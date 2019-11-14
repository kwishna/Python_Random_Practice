# import os
import subprocess as s
# import keyword
import sys
import logging as log


#
# #os.system("E:\\run.bat")
# #os.system('git --version')
# #s.run("E:\\run.bat")
#
# global y
# y = 50
# def outer():
#     x = "local" # local 'x' to outer method
#     global y # Means, This 'y' is global 'y'
#     y = y + 60 # For Modification Of 'y'. It Must Be Declared global. Just For Printing, Declaring global is not required.
#
#     def inner():
#         nonlocal x # nonlocal means 'x' is same as outer def's 'x'
#  #       global y
#         y = 90 # if global 'y' is commented means this 'y' is local.
#         x = "nonlocal"
#         print("inner:", x, y)
#
#         def innerinner():
#             nonlocal  x
#             print('innerinner: ', x, y)
#         innerinner()
#
#     inner()
#     print("outer:", x, y)
#
# outer()
#
# #os.system("E:\\run.bat") # To Execute On Command Line
# # # None Is an Object of NoneType class
# # print(range.__doc__) # For Printing doc of any object
# #
# # for i in keyword.kwlist:
# #     print(i)
# #     print(i.__doc__, end="\n")
#
# # 0 means 'False' and 1 means 'True'
#
# # continuation character (\) : for multiline
# # without continuation char. square or braces can be used for continuation
# a = (1 + 2 + 3 +
#     4 + 5 + 6 +
#     7 + 8 + 9)
# f = open('t.txt', 'w')
# print(a, file=f)

# print(eval('2+3+2'))
# print(int(2+3+3))
# for i in sys.path:
#     print(i)

# print(256 is int("256"))  # Returns True
# print(257 is int("257"))  # Returns False
# print(-5 is int("-5"), id(-5), id(int("-5")))

##########################################################
# def testFunction(a):
#     print("Test", a)
#
#
# y = testFunction
# y(2)
# print(y)
###########################################################
# class Foo:
#     def __call__(self):
#         print('Print Something')
#
# print(callable(Foo))
# InstanceOfFoo = Foo()
# InstanceOfFoo()
###########################################################
# class Hello:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def hey(cls, name, age):
#         cls.name = name
#         cls.age = age
#         print(cls.name, cls.age)
#         print("Hello Class")
#
#     def omg(self):
#         print(self.name, self.age)
#
# Hello.omg(Hello('Krish', 10))
# Hello.hey('Krishna', 20)
# Hello.omg()

###########################################################
# f = open('python.txt', 'r')
# print(f.read())
# print(f)

###########################################################
# class Alpha(object):
#     def __init__(self, a, b):
#         super().__init__()
#         print(a+b)
#
#     def __call__(self, *args, **kwargs):
#         print("Called")
#
# if __name__ == "__main__":
#     a = Alpha(1, 2)
#     a(1,2)

###########################################################