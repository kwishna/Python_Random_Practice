number_one = int(input('Enter A Number : '))
number_two = int(input('Enter Another Number : '))
print(number_one + number_two)
print("The Result Is : " + str(number_one + number_two))

data = int(input("Enter a number: "), 2)  # Enter 10101
print(data)

num1, num2 = map(int, input("Enter Value : ").split())  # Now, User Must Send 2 Values With Space
print(num1 + num2)

num1, num2 = input("Enter Value : ").split()  # Now, User Must Send 2 Values With Space
print(num1 + num2)

# Variable Declaration
a, b, c = 1, 2, 3
print(a + b + c)

a = b = c = 3
print(a + b + c)

a, b, b = 5, 4, 3
print(a + b + b)

x, y, z = 1, 2, 3
print(x, y, z)

txt = ('A', 1, 'Mama')
l, m, n = txt
print(l, m, n)

txt2 = ('A', 'B', 'Drama', 1, 'Mama')
l1, *m1, n1 = txt2
print(l1, m1, n1)