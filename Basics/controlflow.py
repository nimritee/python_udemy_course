#Comparison Operator

num1 = 3
num2 = '3'
print('Are the two number same? ', num1 == num2)
print('Are the nunbers not same? ', num1 != num2)

#Logical Operator

print('Logical Operation 1: ',(4 > 2) and (5 < 8))
print('Logical Operation 1: ',(4 > 2) or (5 < 8))

#Multiple Logical Operators
print('Logical Operation 1: ',(4 > 2) and (5 < 8) or (8 == 9))

#IF Statement 

if 5>3:
    print("My first python flow control operation")
    print('I am being executed')
    if 8 > 0:
        print('Second if block')

#IF - ELSE Statement 

if 6 > 8:
    print('If passed correct operator')
else:
    print('I have not passed the correct operator')

#ELIF Statement

if 8 > 10:
    print('YO - 1')
elif 9 > 10:
    print('YO - 2')
elif 10 > 10:
    print('YO - 3')
else:
    print('Nothing')


# For Loops in a LIST

mylist = [1,2,3,4,5,6]

for items in mylist:
    print('My item:',items)

# For Loops in a Dictionary

mydictionary = {"rahul":1,"chetan":2,"viraj":3}

for items in mydictionary:
    print(items) # This prints all the keys in any order 
    print(mydictionary[items]) # This will print the corresponding value

#Foor Loop in a Tuple

mytuple = [(1,2,3),(4,5,6),(7,8,9)]

for item in mytuple:
    print(item)

#For Loop Tuple unpacking

mytuple1 = [(1,2,3),(4,5,6),(7,8,9)]

for tup1,tup2,tup3 in mytuple1:
    print(tup1)
    print(tup2)
    print(tup3)

#While Loop

i = 1

while i < 5:
    print('The value of I is: {}'.format(i))
    i = i+1

#Range 

for items in range(4,21,2):
    print('I am number {}, from the range'.format(items))

#Without List Comprehension 

x = [1,2,3,4]
out =[]

for num in x:
    out.append(num**2) # number to the power of 2 

print(out)

# With List Comprehension 

x = [1,2,3,4]

out = [num **2 for num in x]
print(out)
