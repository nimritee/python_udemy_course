#Basic Function declaration 

def my_func(param1 = 'Nimritee'):

    '''
    This is a Documnet String by Nimritee
    '''
    print("Have a good day {}!".format(param1))

my_func()

def testing_code():
    '''
    This the function used for Testing 
    '''
    print("Hello World")

testing_code()

#Function to return a value

def return_func():
    return "Good Day"

output = return_func()
print(output)


#To check the type and Calculate sum of integers

def addition(num1,num2):
    '''
    Function to add two numbers.
    '''
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry I need Integers!"

print(addition(4,5))


#Filter 

mylist = [1,2,3,4,5,6,7,8]

def even_num(num):
    return num % 2 == 0

even_numbers = filter(even_num,mylist)
print(list(even_numbers))

#Lambda Expression 

lambda num: num % 2 == 0 
even_num_list = filter(lambda num: num % 2 == 0,mylist)
print(list(even_num_list))

#IN Keyword

print(5 in [1,3,5,6,7])