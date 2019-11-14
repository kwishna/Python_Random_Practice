def add_two(a, b):
    return a + b


def show_last_index(a):
    print(a[-1])


def odd_or_even(a):
    if a % 2 is 0:
        return 'Even'
    return 'Odd'


def is_even(a):
    return a % 2 is 0  # Retuns True Of False


def greatest(a, b, c):
    if a > b and a > c:
        print(f"{a} Is Greatest")

    elif b > a and b > c:
        print(f'{b} Is Greatest')

    else:
        print(f'{c} Is Greatest')


def is_palindrome(a):
    reverse = a[::-1]
    if a == reverse:
        return True
    else:
        return False


def is_palindrome(a):
    return a[::-1] == a



val1 = input('Enter First Value : ')
val2 = input('Enter Second Value : ')
result = add_two(val1, val2)
print(result)

print(show_last_index('Krishna'))

print(odd_or_even(232321))
print(is_even(1))
greatest(10, 525, 515)
print(is_palindrome('malayalam'))
