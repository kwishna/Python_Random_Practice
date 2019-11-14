class Student:
    age = 25 # This Is Class Variable

    def __init__(self, first, last):
        self.first = first  # Instance Variable
        self.last = last    # Instance Variable

    @property
    def info(self):
        print(f'Age Is {self.age}, First Name Is {self.first}, Last Name Is {self.last}')

    @classmethod
    def changeAgeForAll(cls, age):  # This Method Is Class Method. Hence 1st Argument Is Always Class
        cls.age = age
        print(f"Changing The Class Variable Age To {cls.age} For All The Instances Of This Class.")

    @classmethod
    def provideInstance(cls, stri):  # This Method Is Class Method. It Can Be Used To Create An Instance From An String
        first, last, age = stri.split("-")
        return cls(first, last, age) # Creating An Instance Of Class From A Given String

    @staticmethod
    def printSomeThing():
        print("Static : Static Method Doesn't Accept Class Or Instance Variable Implicitly")

    def changeFirstName(self, newFirstName):
        self.first = newFirstName

    def changeLastName(self, newLastName):
        self.last = newLastName

    def changeAge(self, age):
        self.age = age

if __name__ == "__main__":

    stu_one = Student("Krishna", "Singh")
    stu_two = Student("Hello", "World")

    stu_one.info
    Student.printSomeThing()
    stu_one.changeFirstName("Krishna Ji")
    stu_one.changeLastName("Singh Ji")
#    stu_one.changeAge(16)

    stu_one.info
    stu_two.info

    Student.changeAgeForAll(20)

    stu_one.info
    stu_two.info