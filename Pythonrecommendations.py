# -*- coding: utf-8 -*-
"""
Created on 2017/11/16 9:36

@author: Tidus
"""
from math import sqrt
critics = {'Lisa Rose':{'Lady in the Water':2.5,'Snakes on a Plane':3.5,'Just My Luck':3.0,
                        'Superman Returns':3.5,'You,Me and Dupree':2.5,'The Night Listener':3.0},

           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,
                            'Superman Returns': 5.0, 'The Night Listener': 3.0,'You,Me and Dupree': 3.5},

            'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                 'Superman Returns': 3.5, 'The Night Listener':4.0},

            'Claudia Puig': { 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,'Superman Returns': 4.0,
                              'The Night Listener':4.5,'You,Me and Dupree':2.5},

            'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0,
                             'Superman Returns': 3.0, 'The Night Listener':3.0,'You,Me and Dupree':2.0},

            'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Superman Returns': 5.0,
                              'The Night Listener':3.0,'You,Me and Dupree':3.5},

            'Toby': {'Snakes on a Plane': 4.5,'Superman Returns': 4.0, 'You,Me and Dupree':1.0}}

#欧几里得距离
def sim_distance(prefs, person1, person2):
 si={}
 for item in prefs[person1]:
  if item in prefs[person2]:
   si[item] = 1

 n = len(si)
 if n == 0:
  return 0

 sum_of_squares= sum([pow(prefs[person1][item]-prefs[person2][item],2)
                      for item in prefs[person1] if item in prefs[person2]])

 return 1/(1+sum_of_squares)

#皮尔逊相关度
def sim_pearson(prefs, p1, p2):
 si={}
 for item in prefs[p1]:
  if item in prefs[p2]:
   si[item] = 1


 n = len(si)
 if n == 0:
  return 1

 sum1 = sum([prefs[p1][it] for it in si])
 sum2 = sum([prefs[p2][it] for it in si])

 sum1sq = sum([pow(prefs[p1][it],2) for it in si])
 sum2sq = sum([pow(prefs[p2][it],2) for it in si])

 pSum = sum(prefs[p1][it]*prefs[p2][it] for it in si)

 num = pSum-(sum1*sum2/n)
 den = sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
 if den ==0: return 0

 r = num/den
 return r

def topMatches(prefs, person, n=5, similarity = sim_pearson):
 scores = [(similarity(prefs, person, other), other)
           for other in prefs if other != person]

 scores.sort()
 scores.reverse()
 return scores[0:n]

def getRecommendations(prefs, person, similarity = sim_pearson):
 totals = {}
 simSums = {}
 for other in prefs:
  if other == person:
   continue
  sim = similarity(prefs, person, other)
  if sim <=0:
   continue
  for item in prefs[other]:
   if item not in prefs[person] or prefs[person][item] == 0:
    totals.setdefault(item, 0)
    totals[item] += prefs[other][item]*sim
    simSums.setdefault(item, 0)
    simSums[item] += sim
 rankings = [(total/simSums[item], item) for item, total in totals.items()]

 rankings.sort()
 rankings.reverse()
 return rankings

def transformPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person] = prefs[person][item]
	return result

def calculateSimilarItems(prefs, n=10):
	result = {}
	itemPrefs = transformPrefs(prefs)
	c = 0
	for item in itemPrefs:
		c += 1
		if c%100 == 0:
			print('%d / %d'%(c,len(itemPrefs)))
		scores = topMatches(itemPrefs,item,n=n,similarity=sim_distance)
		result[item] = scores
	return result

def getRecommendedItems(prefs,itemMatch,user):
	userRatings = prefs[user]
	scores = {}
	totalSim = {}

	for (item, rating) in userRatings.items():
		for(similarity, item2) in itemMatch[item]:
			if item2 in userRatings:
				continue
			scores.setdefault(item2, 0)
			scores[item2] += similarity*rating

			totalSim.setdefault(item2, 0)
			totalSim[item2] += similarity

		rankings = [(score/totalSim[item],item) for item, score in scores.items()]
		print(rankings,'\n',totalSim)
		print(scores)

		rankings.sort()
		rankings.reverse()
		return rankings
