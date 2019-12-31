# Class Method :-
class Person:
    age = 25

    def printAge(cls):
        print('The age in printAge(cls) is:', cls.age, type(cls))

    @classmethod
    def krishna(cls):  # This Method Is Class Method. Hence 1st Argument Is Always Class
        print("Type Of The 1st Argument Passed In @classmethod krishna(cls) Is : ", type(cls))

    @staticmethod
    def kaba(cls):
        print('Type Of The 1st Argument In kaba(cls) : ', type(cls))

    def baba(cls):
        print('Type Of The 1st Argument In baba(cls) : ', type(cls))

    def raba(self, k):
        print('Type Of The 1st Argument In raba(cls) : ', type(k))

#    def saba():
#        print("It Is Just A Method")

# create printAge class method
Person.printAge = classmethod(Person.printAge)  # Instead We Can Use @classmethod Over printAge(cls) Method.
Person.printAge()  # No Argument Is Required To Pass As It Is classmethod. Hence, 1st Argument By Default Passed As The Class Name
Person.krishna()
# Person.krishna("Krishna") # Error Because, As Per Python. We Are 2 Passing Argument. 1st Argument Class Is By Implicitly Passed.
Person.baba("Krishna")  # 1st Argument Is String. Because It Is Not A classmethod.
Person().kaba(4)
print(type(Person().baba))
print(type(Person().kaba))
print(type(Person().krishna))
print(type(Person().raba))

"""
Here, we have a class Person, with a member variable age assigned to 25.
We also have a function printAge which takes a single parameter cls and not self we usually take.
cls accepts the class Person as a parameter rather than Person's object/instance.
Now, we pass the method Person.printAge as an argument to the function classmethod. This converts the
 method to a class method so that it accepts the first parameter as a class (i.e. Person).
In the final line, we call printAge without creating a Person object like we do for static methods. This prints the class variable age.
"""

from datetime import date


# random Person
# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


class Man(Person):
    sex = 'Male'


man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))
