def hello(a: int, b: float) -> str:
    return str(a) + str(b)
##########################################################
import os
print(os.path.basename("http://inst.eecs.berkeley.edu/~cs61a/fa18/assets/slides/36-Natural_Language_8pp.pdf"))
##########################################################
import random
li = []
for i in range(10):
    var = random.triangular(low=10, high=20, mode=80)
    li.append(var)
print(li)
############################################################
empName = ['Jhon', 'Emma', 'Kelly', 'Jason']
empSalary = [7000, 6500, 9000, 10000]

mapIndexPosition = list(zip(empName, empSalary))
random.shuffle(mapIndexPosition)
empName, empSalary = zip(*mapIndexPosition)

print("List Employee Names: ", empName)
print("List Employee Salary: ", empSalary)
############################################################
# print('Interest Calculator:')
# amount = float(input('Principal amount ?'))
# roi = float(input('Rate of Interest ?'))
# years = int(input('Duration (no. of years) ?'))
# total = (amount * pow(1 + (roi/100), years))  # principle * pow(1 + ((rate/n)/100), (n*time))
# interest = total - amount
# print('\nInterest = %0.2f' %interest)
###########################################################
import pprint as p
d = {x:y for x, y in enumerate(range(5), 0)}
print(d)
p.PrettyPrinter(indent=4).pprint(sorted(d, reverse=False))
##########################################################
from functools import wraps
def some():
    def decorator_name(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not can_run:
                return "Function will not run"
            return f(*args, **kwargs)
        return decorated
    return decorator_name

@some()
def func():
    return("Function is running")

can_run = True
print(func())


# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # Open the logfile and append
#             with open(logfile, 'a') as opened_file:
#                 # Now we log to the specified logfile
#                 opened_file.write(log_string + '\n')
#         return wrapped_function
#     return logging_decorator
#
# @logit()
# def myfunc1():
#     pass
# myfunc1()
######################################################################################
from collections import defaultdict
import json
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
print(json.dumps(some_dict))