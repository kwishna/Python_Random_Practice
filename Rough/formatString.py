print ("{}, A computer science portal for geeks.".format("GeeksforGeeks"))
print("{}, is a {} science portal for {}".format("GeeksforGeeks", "computer", "geeks"))
print("Every {3} should know the use of {2} {1} programming and {0}".format("programmer", "Open", "Source", "Operating Systems"))
print("{gfg} is a {0} science portal for {1}".format("computer", "geeks", gfg ="GeeksforGeeks"))

print('#########################################################################################')

"""
s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation
"""

print ("This site is {0:f}% securely {1}!!".format(100, "encrypted"))
print ("This site is not {0:e}% securely {1} fit!!".format(100000000, "encrypted"))
print ("This site is not {0:15e}% securely {1} fit!!".format(100000000, "encrypted"))
print("The {0} of 100 is {1:b}".format("binary", 100))

print('#########################################################################################')

"""
<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
"""

print("{0:4}, is the computer science portal for {1:8}!".format("GeeksforGeeks", "geeks"))
print("It is {0:5} degrees outside !".format(40))
print("{0:4} was founded in {1:16}!. Yes!".format("GeeksforGeeks", 2009))
print("{0:^16} was founded in {1:<6}!".format("GeeksforGeeks", 2009))
print("{:*^20s}".format("Geeks"))

print('#########################################################################################')

print("Lets Try {:5d}".format(5))