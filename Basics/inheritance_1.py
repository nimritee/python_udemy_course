class Animal():

    def __init__(self):
        print("Animal Class")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("Eating")

class Dog(Animal): # By passing Animal(Class) in the parameter we can inherit the class

    def __init__(self):
        # Animal.__init__(self) #There is no need we can inherit without pasisng this statement also
        print('Dog Class')
    
    def bark(self):
        print("Woof")

    def eat(self): #We are not overridding the animal class eat method
        print("Dog Eating")


my_animal = Animal() #This statement will print; what is there in __init__()
my_dog = Dog()
my_animal.who_am_i() #I am an Animal
my_animal.eat() #Eating
my_dog.who_am_i() # I am an Animal # -> Even if it does not have this method, it gives this output because of Inheritance
my_dog.bark()
my_dog.eat() #-> This will result into its own method eat