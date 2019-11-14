def hello_fun(*args) : # Here Any Number Of Arguments Can Be Passed. As Tuple
    print(type(args))
    print(args)

    if type(args) is tuple :
        print(args[0])

        if type(args[0]) is tuple or list:
            print(args[0][0])

    return True

hello_fun(["sdas", True, 2, 4])

print('********************************')

result = hello_fun(("sdas", True, 2, 4))

print('********************************')

print('Is Task Completed : ', result)