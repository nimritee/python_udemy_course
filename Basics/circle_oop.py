class Circle():

    #Creating pi as the Class Object Attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius #Radius has been created as the class attribute

    #Creating a Method of the class Circle
    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_radi):
        self.radius = new_radi

mycircle = Circle(3)
new_radi = int(input('What is the new radius: '))
mycircle.set_radius(new_radi)
print(mycircle.area())