# -*- coding: utf-8 -*-
"""
Created on 2017/10/29 21:11

@author: Tidus
"""
import re
from collections import Counter
import string

r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'


def checkio(text):
    text = text.lower()
    text = text.replace(' ', '')
    text = re.sub(r, '', text)
    text = [x for x in text if not str(x).isdigit()]
    a = Counter(text)
    for x in a.values():
        if x > 1:
            m = list(zip(Counter(text).keys(), Counter(text).values()))
            t = Counter(text).values()
            t = max(t)
            res = []
            for i in range(len(m)):
                if m[i][1] == t:
                    res.append(m[i][0])
            res = list(map(ord, res))
            res.sort()
            return chr(res[0])

    res = []
    for x in text:
        res.append(x)
    res = list(map(ord, res))
    res.sort()
    # print(chr(res[0]))
    return chr(res[0])


    # replace this for solution


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
