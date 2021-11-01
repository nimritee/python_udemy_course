from datetime import date
from datetime import datetime
from os import kill

class User():

    def __init__(self,firstname,dateOfBirth):
        self.firstname = firstname
        self.dateOfBirth = dateOfBirth
    
    def getFirstname(self):
        return self.firstname

    def setFirstname(self,newname):
        self.firstname = newname
    
    def getAge(self):
        today = date.today()
        dob = datetime.strptime(self.dateOfBirth, '%m-%d-%Y').date()
        years = today.year - dob.year - ((today.month,today.day) < (dob.month,dob.day))
        age = "{} Years".format(years)
        return age

username = input("Hello, Please enter your first name: ")
dob = input("Hi {}, please enter your birthdate in 'MM-DD-YYYY' format.\n".format(username))
myuser= User(username,dob)

print('The first name of the user is: ', myuser.getFirstname())
newname = input('Enter the new user name: ')

changeUsername = myuser.setFirstname(newname)
print('The first name of the user has been updated to:', myuser.getFirstname())
print('The age of the user is:', myuser.getAge())