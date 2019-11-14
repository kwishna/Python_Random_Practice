from collections import Counter
from typing import Any

listt = [1, 1, 2, 3, 1, 1, 2, 3, 2, 1, 2, 3, 1, 2]
print("counter(list) Returns Number Of Times Each Elements Has Occurred :: ", Counter(listt))   # Counter({1: 6, 2: 5, 3: 3})

word = "he is a good person. very good person he is but not so so good person."
list_of_words = word.split()
print("Number of times each word occurs are :: ", Counter(list_of_words))   # Counter({'good': 3, 'he': 2, 'is': 2, 'person.': 2, 'so': 2, 'a': 1, 'very': 1, 'person': 1, 'but': 1, 'not': 1})

lists_of_letters = list(word)
print("List of letters in the word :: ", lists_of_letters)
print("Occurance of each letter in the word is :: ", Counter(word))

c = Counter(lists_of_letters)  # Here c is in form of a dict
print("3 most common in the words are :: ", c.most_common()[:3:1])
print("3 least common in the words are :: ", c.most_common()[:-4:-1])
print("Total numbers in counter :: ", c.values())
print("Total numbers of 'o' in counter :: ", c['o'])
print("List Of The Counter Values :: ", list(c))
print("Set Of The Counter Values :: ", set(c))
print("Dictionary Of The Counter Values :: ", dict(c))
print("Tuple Of The Counter Values :: ", tuple(c))
print("Items In c :: ", c.items())
c.clear()
print("All Values In c after clear :: ", c.values())  # Prints dict_values([])

c1 = Counter(a=4, b=2, c=0, d=-2, o=5)
sorted(c1.elements())  # prints : ['a', 'a', 'a', 'a', 'b', 'b']
c1['a'] = 5  # Setting Count Of 'a'
print("Count Of 'a' Is Increased To 5. As We Have Set It :: ", c1)
## We Can Add And Subtarct 2 Counters


c2 = Counter({'a': 2, 'b': 2, 'c': 3, 'o': 4, 'd': -1})
print("Intersection of c & c1 :: ", c2 & c1)  # intersection:  min(c[x], d[x]) # doctest: +SKIP
print("Intersection of c & c1 :: ", c2 | c1)  # union:  max(c[x], d[x])

d = {"one": 1, "two": 2, "three": 3, "four": 4}
d.update(red='b', blue=2, one='5')
print('Updated Dictionary ::', d)
dict(a=1, b=2, c=3)
