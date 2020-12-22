class Person:

    def __init__(self, name, age):  # class constructor
        self.name = name
        self.age = age


obj1 = Person("Deb", 31)
print("The name is {a} having age {b}".format(a=obj1.name, b=obj1.age))

