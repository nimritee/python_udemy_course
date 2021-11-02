from datetime import date
from datetime import datetime
import datetime as dt

class User():

    def __init__(self,firstname,dateOfBirth):
        self.firstname = firstname
        self.dateOfBirth = dateOfBirth

    def getFirstname(self):
        return self.firstname

    def setFirstname(self,newname):
        self.firstname = newname
    
    def validDate(self):
        isValid = True
        month,day,year = self.dateOfBirth.split('-')
        try:
            dt.datetime(int(year), int(month), int(day))
        except ValueError:
            isValid = False
        return isValid

    def getAge(self):
        dob =  datetime.strptime(self.dateOfBirth, '%m-%d-%Y').date()
        today = date.today()
        years = today.year - dob.year - ((today.month,today.day) < (dob.month,dob.day))
        return ("The age of the user is: {} Years".format(years))


username = input("Hello, Please enter your first name: ")
dob = input("Hi {}, please enter your birthdate in 'MM-DD-YYYY' format.\n".format(username))
myuser= User(username,dob)

if myuser.validDate():
    print('The first name of the user is: ', myuser.getFirstname())
    newname = input('Enter the new user name: ')
    changeUsername = myuser.setFirstname(newname)
    print('The first name of the user has been updated to:', myuser.getFirstname())
    print(myuser.getAge())

else:
    print("Please provide a valid Date of Birth, in the proper format")