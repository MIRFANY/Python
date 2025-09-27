class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)




#use the person class to create an objectm and then execute the  printname method:


x= Person("John ", "irfan")


x.printname()


#create a cild class and inside that write an __init__() function
class Student(Person):
    def __init__(self, fname, lname):







