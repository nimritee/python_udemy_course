from datetime import date
from datetime import datetime

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
        birthdate = datetime.strptime(self.dateOfBirth, '%m-%d-%Y').date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

myuser= User('Nimritee','11-22-1997')
print('The first name of the user is:', myuser.getFirstname())
newname = input('Enter the new user name: ')
changeUsername = myuser.setFirstname(newname)
print('The first name of the user has been updated to:', myuser.getFirstname())
print('The age of the user is:', myuser.getAge(),"Years")
