def occourances(character1,filepath):
    with open(filepath) as myfile:
        content = myfile.read()
    
    return content.count(character1)
    
character1 = input("Enter the character: ")
count = occourances(character1,"fruits.txt")
print(count)
    

# with open("bear.txt") as myfile:
#     content = myfile.read()
    
# transferdata = content[:90]
# with open("first.txt","w") as myfile1:
#     myfile1.write(transferdata)
