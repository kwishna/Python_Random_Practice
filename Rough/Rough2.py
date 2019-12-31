def mama(s: 'in float', m: "in integer") -> "in float":
    return s + m


def nama(s: float, m: int) -> float:
    return s + m


print("Annotations In mama Method Are : ", mama.__annotations__)
print("Annotations In nama Method Are : ", nama.__annotations__)


def kinetic_energy(m: 'in KG', val: 'in M/S') -> 'in Joules':
    return 1 / 2 * m * val ** 2


print("Annotations In kinetic_energy Method Are : ", kinetic_energy.__annotations__)
print("**************************************************")

## ----------------------------------------------------------------
result = 100 / 777
print('Result Of 100/777 is : ', result)
print("The Value Is {r:1.2f}".format(r=result))
print("The Value Is {0:1.2f}".format(result))
print("**************************************************")

## ----------------------------------------------------------------
dict_one = {1: 'A', 2: 'B', 3: "C", 3: "E"}  # Duplicates Only Once
print('Dictionary Value For Key 1 In', dict_one, " Is -> ", dict_one[1])
print("**************************************************")

## ----------------------------------------------------------------
t = ('1', '2', '3', '4', '1')
print("Index of 4 in t In : ", t, " Is : ", t.index('4', 1))
print("**************************************************")

## ----------------------------------------------------------------
setA = set()
setA.add('A')
setA.add('B')
setA.add('C')
setA.add("D")

setB = {'a', 'b', 'c', 'd'}
print('Two Sets Are :: ', setA, setB)
print("**************************************************")

## ----------------------------------------------------------------
myList = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in myList:
    print("The Sum For Each Iteration Is : ", a + b + c)
print("**************************************************")

## ----------------------------------------------------------------
dict_two = {1: 'A', 2: 'B', 3: "C", 3: "E"}  # Duplicates Only Once
print("Dictionary Is : ", dict_two)
if "A" in dict_two:
    print("Value 'A' found in dictionary")
else:
    print("Value 'A' not found in dictionary")

del (dict_two[1])
print("After Doing del(dict[1]) : ", dict_two)

## for k, v in dict throws error. cannot unpack error.
for k, v in dict_two.items():
    print(f"for key : {k} and value : {v} in dict_two.")
print("**************************************************")

## ----------------------------------------------------------------
list_one = list(range(10))
print("List Created By 'list(range(10))' Is : ", list_one)
print("**************************************************")

## ----------------------------------------------------------------
for items in enumerate(['A', 1, 'Apple', {'A': 1, 'B': 2, 'C': 3}, (0, 1), {1, 'A', 'B'}]):
    print("Enumerated Items Are : ", items, ' & Type Of 2nd Arg Is : ', type(items[1]))
print("**************************************************")

## ----------------------------------------------------------------
letters = "Hello Python"
list_two = [x for x in letters]
print("The Created List Is : ", list_two)

list_three = [x for x in letters if x != " "]
print("The Created List Is : ", list_three)

list_four = [x if x != " " else None for x in letters]
print("The Created List Is : ", list_four)

list_four.pop()  # Removes Last Items
print("The List After pop() : ", list_four)

list_four.pop(3)  # Removes Last Items
print("The List After pop(3) : ", list_four)
print("**************************************************")

## ----------------------------------------------------------------
## Convert Every Odd Letter In Caps :-
def myfunc(rgs):
    """
    :rtype: str
    """
    ran = ""
    for i in range(rgs.__len__()):
        if i % 2 == 0:
            ran += rgs[i].upper()
        else:
            ran += rgs[i].lower()
    return ran

print("Alternate CAPS & small : ", myfunc("AppPkle"))
print("**************************************************")

## ----------------------------------------------------------------
import re

stri = 'nbdJBG JWDd#bwk!ajdb d'
hi = re.split(pattern='[^a-zA-Z0-9\s]', string=stri)
print("Using Regex Split : ", hi)

print("Reverse An String : ", stri[::-1])
print("**************************************************")

## ----------------------------------------------------------------
def sq(num):
    return num ** 2


list_five = [1, 2, 3, 4, 5]
square = map(sq, list_five)
for i in square:
    print("Using map(fun, iterable) : ", i)

print("List Using map(func, iterable) : ", list(map(sq, list_five)))


def evenOrOdd(val):
    if len(val) % 2 == 0:
        return {val: 'EVEN'}
    else:
        return {val: 'ODD'}

list_six = ["Krisna", "Apple", "Boy", "Eagle", "Donkey"]
print("List Using map() :-\n", list(map(evenOrOdd, list_six)))
print("**************************************************")

## ----------------------------------------------------------------
def even_odd(val):
    if len(val) % 2 == 0:
        return True
    else:
        return False

list_seven = ["Krisna", "Apple", "Boyy", "Eagle", "Donkey"]
fil = filter(even_odd, list_seven)
print("List using filter() : ", list(fil))
print("**************************************************")

## ----------------------------------------------------------------
## lambda
def square(num):
	return num**2
## Convert To lambda
s = lambda x : x**2
print("Using Lambda : ", s(9))

list_eight = [1, 2, 3, 4, 5]
print("Using lambda In map() : ", list(map(lambda x : x**2, list_eight)))

print("**************************************************")

## ----------------------------------------------------------------
scope = "GLOBAL"
def outer():
    scope = "OUTER FUNCTION"

    def inner():
        scope = "INNER FUNCTION"
        print("scope variable is from : ", scope)
    inner()
outer()
print("GLOBAL SCOPE : ", scope)
print("**************************************************")

## ----------------------------
## After Commenting Inner scope
scope = "GLOBAL"
def outer():
    scope = "OUTER FUNCTION"

    def inner():
#       scope = "INNER FUNCTION"
        print("scope variable is from : ", scope)
    inner()
outer()
print("GLOBAL SCOPE : ", scope)
print("**************************************************")

## -------------------------------
## After Commenting Outer Scope As Well
scope = "GLOBAL"
def outer():
#    scope = "OUTER FUNCTION"

    def inner():
#        scope = "INNER FUNCTION"
        print("scope variable is from : ", scope)
    inner()
outer()
print("GLOBAL SCOPE : ", scope)
print("**************************************************")

## ----------------------------
## After Commenting Inner scope
scope = "GLOBAL"
def outer():
    global scope
    scope = "OUTER FUNCTION"
    scope2 = "OUTER FUNCTION 2"

    def inner():
        nonlocal scope2
        global scope
        scope = "INNER FUNCTION"
        print("scope & scope2 variable is from : ", scope, ",", scope2)
    inner()
outer()
print("GLOBAL SCOPE : ", scope)
print("**************************************************")

##------------------------------------------------------
import string
sample = 'My Name Is Anthony Gonsalves'
print("Does The Line Contains All The Alphabets : ",set(sample.lower()) >= set(string.ascii_lowercase))
print("**************************************************")

##-----------------------------------------------------
import decimal as d # convert 'e' to floating value using d.Decimal()

new=1
old=0

for i in range(1, 30):
    total = old + new
    new = new * 3
    old = total

print(new)
print(total)

# print((total*6.4799e-5)/(100)) #1, 2, 4, 8, 16, 32
# print(int(result))
# print(format(int(result), "b"))
# print(format(result, ".0f"))
# print("{:1f}".format(result))

# print("{0:50}, is the for {1:8}!".format("GeeksforGeeks", "geeks")) 

##-----------------------------------------------------
'''<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
'''

print("{0:4}, is the computer science portal for {1:8}!".format("GeeksforGeeks", "geeks")) 
print("It is {0:5} degrees outside !".format(40)) 
print("{0:4} was founded in {1:16}!".format("GeeksforGeeks", 2009)) 
print("{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)) 
print("{:*^20s}".format("Geeks"))
print(format(234.998, ".2f"))
#########################################################################
from typing import Literal

def draw_line(direction: Literal["horizontal", "vertical"]) -> None:
    if direction == "horizontal":
        print(direction)

    elif direction == "vertical":
        print(direction)

    else:
        raise ValueError(f"invalid direction {direction!r}")

draw_line("up")
#############################################################################











