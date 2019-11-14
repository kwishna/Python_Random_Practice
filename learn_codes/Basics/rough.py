import random

random_no = random.randint(5, 20)
print(random_no)


def is_palindrome(a):
    a = str(a).lower()
    for i in range(len(a)):
        if (a[0] is a[-1]) and (a[i] is a[-i]):
            return True
        else:
            return False


print(is_palindrome('malyalam'))
