import random

for i in range(10):
    if i is 5: # is Checks Value & Reference As Well. It Works For Small Integers Only
        print('Continued At {}'.format(i))
        continue
    print(i)

print('\n')

for i in range(10):
    if i == 5 :
   # if i is 5: # Use == For Value Compare. 'is' For Reference. 1000 is 10**3 returns False
        print("Breaked")
        break
    print(i)

# Guessing Games
guess = int(input('Please Guess The Number Between 1 & 100 : '))
winning_no = random.randint(1, 100)
i = 0
while True:

    if guess is winning_no:
        i += 1
        if i is 1:
            print('\nSuperb! You Guessed Right In One Go!!!')
        else:
            print('\nCongratulations! You Won!!!')
            print('But, You Tried {} Times To Win'.format(i))
        break

    else:
        if guess > winning_no:
            print('Too High\n')
            # i += 1
            # guess = int(input('Sorry! Please Guess Again : '))

        elif guess < winning_no:
            print('Too Low\n')
            # i += 1
            # guess = int(input('Sorry! Please Guess Again : '))

        else:
            print('Invalid Input\n')
            # i += 1
            # guess = int(input('Sorry! Please Guess Again : '))

        i += 1
        guess = int(input('Sorry! Please Guess Again : '))