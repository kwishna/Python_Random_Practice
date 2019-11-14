i = 1

while i < 5:
    print('Loop Running : Value Of i Is : {}'.format(i))
    i += 1

n = int(input('Enter A Natural Number : '))
summ, i = 0, 1
while i <= n:
    summ = summ + i
    i += 1
print(summ)

no = int(input("Enter A Number Of Multiple Digits : "))
rem, ad = 0, 0
while no>0 :
    rem = no%10
    ad = ad+rem
    no= no//10

print(ad)

##Printing Count Of Characters In A String
while True : # Infinite Loop : CTRL + C To Break The Loop
    my_name = input('Enter Your Name : ')
    my_name = my_name.lower()
    name_length = len(my_name)
    i = 0
    temp = ''
    while i < name_length - 1:
        if my_name[i] not in temp:
            temp = temp + my_name[i]

            p = my_name.count(my_name[i])
            print(f"Count Of {my_name[i]} Is : {p} \n")
        i += 1


y=5
while y in range(10) :
    print(y)
    y+=1