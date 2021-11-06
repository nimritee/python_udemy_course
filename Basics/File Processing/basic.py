myfile= open("fruits.txt") #Takes the path to the file as arguement

#Used to create a file object; and store in a python variable. When the execution starts the object will be craeted, 
#and when the execution ends the object will be deleted.

content = myfile.read() #Reading once and saving the content in the variable, and printing multiple times.

print(content)
print(content)
print(content)

print(myfile.read()) #This is print and empty string, as the file cursor is at its end point.

myfile.close()

with open("fruits.txt") as myfile: #Implicitly closes the file, better way of Programming
    content = myfile.read()

print(content) 

with open("/Users/nimritee/Desktop/sample.txt") as myfile1: # File with a different path
    content1 = myfile1.read()

print(content1)


with open("vegetables.txt","w") as myfile2:
    myfile2.write("Tomato\nPotato\nUmbrealla")
    myfile2.write("Garlic")

# with open("fruits1.txt","x") as file3:
#     file3.write("Okra")

with open("fruits1.txt","a+") as file4:
    file4.write("Nimritee")
    file4.seek(0)
    conetnt6 = file4.read()
    
print(conetnt6)
