name, age = input("Enter Your Name & Age : ").split()
age = int(age)
if int(age) >= 18 and int(age) < 60:
    print(f"Hi {name}! You Are Adult And Young.")

elif age < 10 and age > 0:  # We Can Also Write As 0<age<10
    print(f"Hi {name}! You Are Too Young.")

elif 10 <= age <18:
    print(f"Hi {name}! You Are Still Quite Young.")

elif age <= 0 or age in range(200, 9999999999):
    pass

else:
    print(f"Hey Kid {name}. You Are Too Old Uncle!")


if 'a' in name :
    print(f'Your Name Has "a" at : {str(name).find("a")}')
    print(f'Your Name Has "a" at : {str(name).index("a")}')
    print(f'ASCII Value Is : ', ord('a'))   # ASCII Value Of Any Character

name = "dkdkdahs"
if name :
    print('\nName Is Not Empty ')  # To Check Empty


y=5
if y in range(2,10):
    print("If Loop In The Range")

while y in range(10) :
    print(y)
    y+=1
