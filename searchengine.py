# -*- coding: utf-8 -*-
"""
Created on 2017/11/18 10:58

@author: Tidus
"""
import re
import urllib.request
from bs4 import *
from urllib.parse import urljoin
from sqlite3 import dbapi2 as sqlite

ignorewords = {'the': 1, 'of': 1, 'to': 1, 'and': 1, 'a': 1, 'in': 1, 'is': 1, 'it': 1}

class crawler:
	def __init__(self, dbname):
		self.con = sqlite.connect(dbname)

	def __del__(self):
		self.con.close()

	def dbcommit(self):
		self.con.commit()

	def getentryid(self, table, field, value, createnew=True):
		cur = self.con.execute(
			"select rowid from %s where %s='%s'" % (table, field, value))
		res = cur.fetchone()
		if res == None:
			cur = self.con.execute(
				"insert into %s (%s) values ('%s')" % (table, field, value))
			return cur.lastrowid
		else:
			return res[0]

	def addtoindex(self, url, soup):
		if self.isindexed(url): return
		print('Indexing ' + url)

		# Get the individual words
		text = self.gettextonly(soup)
		words = self.separatewords(text)

		# Get the URL id
		urlid = self.getentryid('urllist', 'url', url)

		# Link each word to this url
		for i in range(len(words)):
			word = words[i]
			if word in ignorewords: continue
			wordid = self.getentryid('wordlist', 'word', word)
			self.con.execute("insert into wordlocation(urlid,wordid,location) values (%d,%d,%d)" % (urlid, wordid, i))

	def addlinkref(self, urlFrom, urlTo, linkText):
		words = self.separateWords(linkText)
		fromid = self.getentryid('urllist', 'url', urlFrom)
		toid = self.getentryid('urllist', 'url', urlTo)
		if fromid == toid: return
		cur = self.con.execute("insert into link(fromid,toid) values (%d,%d)" % (fromid, toid))
		linkid = cur.lastrowid
		for word in words:
			if word in ignorewords: continue
			wordid = self.getentryid('wordlist', 'word', word)
			self.con.execute("insert into linkwords(linkid,wordid) values (%d,%d)" % (linkid, wordid))

	def gettextonly(self, soup):
		v = soup.string
		if v == None:
			c = soup.contents
			resulttext = ''
			for t in c:
				subtext = self.gettextonly(t)
				resulttext += subtext + '\n'
			return resulttext
		else:
			return v.strip()

	def separatewords(self, text):
		splitter = re.compile('\\W*')
		return [s.lower() for s in splitter.split(text) if s != '']

	def isindexed(self, url):
		return False

	def addlinkref(self, urlFrom, urlTo, linkText):
		pass

	def crawl(self, pages, depth=2):
		pass

	def createindextabels(self):
		self.con.execute('create table urllist(url)')
		self.con.execute('create table wordlist(word)')
		self.con.execute('create table wordlocation(urlid,wordid,location)')
		self.con.execute('create table link(fromid integer,toid integer)')
		self.con.execute('create table linkwords(wordid,linkid)')
		self.con.execute('create index wordidx on wordlist(word)')
		self.con.execute('create index urlidx on urllist(url)')
		self.con.execute('create index wordurlidx on wordlocation(wordid)')
		self.con.execute('create index urltoidx on link(toid)')
		self.con.execute('create index urlfromidx on link(fromid)')
		self.dbcommit()

	def crawl(self, pages, depth=2):
		for i in range(depth):
			newpages = {}
			for page in pages:
				try:
					c = urllib.request.urlopen(page)
				except:
					print("Could not open %s" % page)
					continue

				soup = BeautifulSoup(c.read())
				self.addtoindex(page, soup)
				try:
					links = soup('a')
					for link in links:
						if ('href' in dict(link.attrs)):
							url = urljoin(page, link['href'])
							if url.find("'") != -1: continue
							url = url.split('#')[0]  # remove location portion
							if url[0:4] == 'http' and not self.isindexed(url):
								newpages[url] = 1
							linkText = self.gettextonly(link)
							self.addlinkref(page, url, linkText)
					self.dbcommit()
				except:
					print("Could not parse page %s" % page )

			pages = newpages
class searcher:
	def __init__(self, dbname):
		self.con = sqlite.connect(dbname)

	def __del__(self):
		self.con.close()

	def getmatchrows(self, q):
		# Strings to build the query
		fieldlist = 'w0.urlid'
		tablelist = ''
		clauselist = ''
		wordids = []

		# Split the words by spaces
		words = q.split(' ')
		tablenumber = 0

		for word in words:
			# Get the word ID
			wordrow = self.con.execute(
				"select rowid from wordlist where word='%s'" % word).fetchone()
			if wordrow != None:
				wordid = wordrow[0]
				wordids.append(wordid)
				if tablenumber > 0:
					tablelist += ','
					clauselist += ' and '
					clauselist += 'w%d.urlid=w%d.urlid and ' % (tablenumber - 1, tablenumber)
				fieldlist += ',w%d.location' % tablenumber
				tablelist += 'wordlocation w%d' % tablenumber
				clauselist += 'w%d.wordid=%d' % (tablenumber, wordid)
				tablenumber += 1

		# Create the query from the separate parts
		fullquery = 'select %s from %s where %s' % (fieldlist, tablelist, clauselist)
		print(fullquery)
		cur = self.con.execute(fullquery)
		rows = [row for row in cur]

		return rows, wordids

