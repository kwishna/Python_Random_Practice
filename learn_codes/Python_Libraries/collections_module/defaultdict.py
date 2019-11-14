from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import *

k = dict(a=1, b=2, c=3)
##  k[5]  # prints :- throws KeyError

dk = defaultdict(
    object)  # The First Element In The defaultdict Becomes The Default Value And returns Same If There Is Not Value Available For Any Key
print("dk :: ", dk['a'])  # Doesn't Throw KeyError

dk['one']
for i in dk:
    print("keys Are :: ", i)

dk2 = defaultdict(lambda: 0)  # Takes Argument Nothing And Returns 0. This Becomes Default Condition For The Dict.
dk2['1']
dk2['2'] = 5
print("dk2 :: ", dk2)

l = {k: k * k for k in range(5)}
for x in l:
    print("Keys-Values From Generator :: ", x, l[x])
print('------------------------------------------')
#################################################################################################

d = dict(six=6, two=2, one=1, four=4, three=3)  # dict constructor # 2 Dictionaries Whose Keys & Values Are Same But Added In Different Order Is Equal.
for i in d.keys():
    print("dictionary d Values from d -> ", i, d[i]) ## It Will Print The Dict In Un-ordered Way
print("------------------------------------------")

od = OrderedDict() # 2 Ordered Dictionaries Whose Keys & Values Are Same But Added In Different Order Is Unequal.
od['four'] = 6
od['three'] = 5
od['two'] = 4
od['one'] = 3
for i in od.keys():
    print("dictionary od Values from od -> ", i, od[i]) ## It Will Print The Dict In Un-ordered Way
print('------------------------------------------')

Cat = namedtuple('Cat', 'name claws fur')
c = Cat(name='Kitty', claws=True, fur="Furry")
print("Named Tuple :: ", c)

print(c.name)
print(c[2])

print('------------------------------------------')

d = deque("Apple Boy")
d.append(1)
d.append(2)
print(d.maxlen)
print(d)

print('------------------------------------------')

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
ch = ChainMap(adjustments, baseline)
for k in ch:
    print("chained Map :: ", k)