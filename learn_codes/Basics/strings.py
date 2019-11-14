import string
value = 'apple'  # a{0 & -5}, p{1 & -4}, p{2 & -3}, l{3 & -2}. e{4 & -1}
print(value[0])  # a : Indexing In String. Also, There Is Reverse Indexing. Last Character Starts With -1.
print(value[-1])  # e : Printing Last Value When User Doesn't Know Length Of The String.

print(value[0:2])  # ap : String Slicing.
print(value[0:])  # apple : Prints Complete String.
print(value[-5:2])  # ap : Index -6 & 0 Means Same.
print(value[-3:])  # ple
print(value[:3])  # app
print(value[:-4])  # a
print(value[-5:-1])  #

print(value[0:5:2])  # ape : Last Index Is Step Argument.
print(value[::-1])  # elppa : Reverse : Useful : Since, 1st & Last Index Is Blank. It Is 0 & 4 By Default.
print(value[5:0:-1])  # elpp : Reverse
print(value[-1::-1])  # elppa : Reverse

name = 'I Am Anthony Gonsalves'
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count('A'))  # Count Number Of Times 'A' Comes In The String.
print(name.replace('n', 'N'))

sample = '     aap     '
sam = '...'
print(sample + sam)
print(sample.lstrip() + sam)
print(sample.rstrip() + sam)
print(sample.strip() + sam)

fruit = 'a p p l e'
sentence = 'He Is He Is A Sports Person'
print(fruit.replace(' ', ''))  # Removing Middle Space
print(fruit.replace('p', 'P', 1))  # Replacing Only One 'p'
print(sentence.replace("Is", "IS", 1))
print(sentence.find('Is'))  # index Of 'Is'
print(sentence.find('Is', 5))
print(fruit.center(11, '*'))  # 9+2 = 11
print(fruit.center(13, '*'))  # 9+4 = 13
print(fruit.center(12, '*')) # 1 star more in right
# String Is Immutable In Python

fruit += fruit
print(fruit)
print(fruit*2)

s = """ this is a very
        long string if I had the
        energy to type more and more ..."""
print(s)

t =  s = ("this is a very"
        "long string too"
        "for sure ..." )

print(t)