x = 5  # global variable x


def fun():
    x = 7  # local variable x
    return x


def fun2():
    global x  # If We Want To Change The Value Of global variable then we need to declare here. Else, global variable won't be accessible inside any function,
    x = 10    # Now This Is global x
    return x


print(x)
print(fun())
print(fun2())
print(x)
