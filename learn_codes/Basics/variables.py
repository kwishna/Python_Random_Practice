# # Variable Declaration
a, b, c = 1, 2, 3
print(a + b + c)

a = b = c = 3
print(a + b + c)

a, b, b = 5, 4, 8
print(a + b + b)

num1, num2 = input("Enter 2 Values With Space : ").split()  # Now, User Must Send 2 Values With Space
print(int(num1) + int(num2))

num1, num2 = input("Enter 2 Values With Comma : ").split(",")  # Now, User Must Send 2 Values With Comma
print(num1 + num2)

name, age = input("Enter You Name & Age With Comma Separated : ").split(",")
print("Your Name Is " + name + " And Your Age Is " + age)
print("Your Name Is {} And Your Age Is {}".format(name, age)) # String Formatting In Python3
print(f"Your Name Is {name} And Your Age Is {age}") # Python 3.6

num1, num2, num3 = input("Enter 3 Number And I Will Show You It's Average : ").split()
print(f'Average Of {num1} , {num2} & {num3} Is : '+str((int(num1)+int(num2)+int(num3))/3))
print('Average Of {} , {} & {} Is : {} '.format(num1, num2, num3, (int(num1)+int(num2)+int(num3))/3))
print(f'Average Of {num1} , {num2} & {num3} Is : {str((int(num1)+int(num2)+int(num3))/3)}')


