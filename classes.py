class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age




p1 = Person("John", 36)

print(p1.name)
print(p1.age)












class vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return f"{self.name}({self.price})"
    

car1 = vehicle("Alto", 3.5)

print(car1)
# print(car1.price)


class animals:
    def __init__(self, name, categ):
        self.name = name
        self.categ = categ

oggy = animals("Olly","pet")

print(oggy.name)
print(oggy.categ)
        

class Personi:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is "+ self.name)


p1 = Personi("John", 36)
p1.myfunc()



class students:
    def __init__(self, name, enrol):
        self.name = name
        self.enrol = enrol


    def myfunc(self):
        print("hello my name is "+ self.name)


p1 = Person("Irfan", 70)

p1.myfunc()