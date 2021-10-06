# Basics
"Hello" #String in Double Quotes
'Hello' #String in Single Quote

" I'm a student " # Single Quotes inside a Double Quote; could be vice-versa as well.

# Indexing
mystring = "abcdefg"
print(mystring[-1]) #The last element can be accessed like this

# Slicing
    #Beggining, End, Step Size

myslicestring = "abcdefg"
print(myslicestring [1:]) # From index 1 to last
print(myslicestring [:5]) # From index strat until index 5; but does not include index 5
print(myslicestring [1:5]) # From index 1 to 4
print(myslicestring [::]) # Print the entire string
print(myslicestring [::1])
print(myslicestring [::2]) #aceg

# Basic Functions

print(myslicestring.upper()) #Upper Case of all the letter
print(myslicestring.lower()) #Lower Case of all the letter
print(myslicestring.capitalize()) #Used to capitalize the first letter
print(myslicestring.split('d')) # Split on the letter d 

#Print Formatting 
x = "Hi Good Day {Nachname}, {Forname}".format(Nachname="Sirsalewala",Forname="Nimirtee")
print(x)
# y = "Hi {} hhf {}".format("helo","fh")
