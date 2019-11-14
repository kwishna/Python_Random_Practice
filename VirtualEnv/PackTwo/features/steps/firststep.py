from behave import *

@given('I am creating a feature file')
def first_Method(context):
    context.text
    print("Krishna Kumar Singh")

@then('I will create step file')
def secondMethod(context):
    print("Krishna Kumar Singh")

@then('I will create a runner file')
def thirdMethod(context):
    print("Krishna Kumar Singh")

@given('I am creating a {first_name} file')
def firstMethod(context, first_name):
    print(first_name)

@then('I will create a {middle_name} step file')
def secondMethod(context, middle_name):
    print(middle_name)

@then('I will create a {last_name} runner file')
def thirdMethod(context, last_name):
    print(last_name)
