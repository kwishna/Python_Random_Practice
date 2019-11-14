print("Hello Python In Double Quotes")
print('Hello Python In Single Quotes')
print("Hello 'Python' Again")
print('Hello "Python" Again')
# print('Hello 'python' Hello') : Cannot User Single Quote Inside Single Quote, Sytax Error
# print("Hello "python" Hello") : Cannot User Double Quote Inside Double Quote, Sytax Error
print("1st line\n2nd line")
print('Escape Sequence\'s Writing with \\ Back Slash & double black slash \\\\. Also err\basing one \'r\'')
print('We Can Comment A Line By Using #')
print("Use CTRL+\\ To Comment Whole Line If U Forgot To Add # Before The Line")
print('printing escape sequence \\n in terminal')
print('This Is Mountain /\\/\\/\\/\\/\\/\\/\ ')
print('Print \t\t Spaces')
print('emoji 🤭')
print('\U0001F93B')  # Printing Emojis By Unicode
data = int("502", 10)  # Decimal
print(data)
data = int("10101", 2)  # binary to decimal
print(data)
########################################################
print(4 / 3)  # Float Division
print(4 // 3)  # Integer Division
print(0 / 1)
print(2 * 3) # 6
print(2 ** 3) # 8
print(round(2 / .3))
print(2 / 0.3)
print(2 / 0.3, 3)
print(round(2 / .3, 3))  # Round Off To 3 Decimal Digits Only.
print(1, 2, 3, sep="-")

for i in range(10):
    print(i)  # By Default It Prints In New Line.
for i in range(10):
    print(i, end=' ')  # Now It Will Put Space For Each Print.

print('\n'+3 % 2)
print(2 ** 3 ** 2)
###########################################################
first_name = 'Kr'
last_name = "Sn"
full_name = first_name + last_name
print(full_name)
print(first_name + " " + last_name)
print(first_name + str(3))
print(first_name * 3)
#############################################################
num = 2
print(num)
num = 'abd'
print(num)
# Variable Can't Start With Numbers.
# Can Start With Underscore _, letters.
# No Special Characters Anywhere
# Naming Convention : Seperate With Underscore When Multiple Words Are There
##############################################################
# User Input
name = input('Please Type Your Name : \n')  # Input Comes In String Only
print('Welcome! ' + name)
###############################################################
