def details(first_name, last_name, age) : # We Any Parameter Is Not Passed. Python Will Throw Error
    print(f'First Name Is : ', first_name)
    print(f'Last Name Is : ', last_name)
    print(f'Age Is : ', age)


def detail(first_name, last_name, age = None) : # It Will Not Throw Error If age Is Not Passed As Parameter.
    print(f'First Name Is : ', first_name)  # None Means null.
    print(f'Last Name Is : ', last_name)
    print(f'Age Is : ', age)

# def detail(first_name, last_name="Something", age) # Wrong
# This Is Wrong. All Arguments In RHS To Default Param(last_name) Should Also Be Default Param.
# def detail(first_name, last_name="Something", age=24) # Correct
# def detail(first_name="Anything", last_name="Something", age=24) # Correct
# def detail(first_name=None, last_name=, age=24) # Wrong

details('Krishna', 'Singh', 24)
detail('Krishna', 'Singh')