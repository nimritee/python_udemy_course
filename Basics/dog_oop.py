class Dog():

    species = "mammals"

    def __init__(self,breed,name):
        self.breed = breed
        self.name =name
    
mydog = Dog(breed='Lab',name='sammy')

print(mydog.breed)
print(mydog.name)
print(mydog.species)