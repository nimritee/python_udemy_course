x = 25 

def my_func():
    x=50
    return x

my_func()
print(x)

## The output of the above problem will be x = 25 and not 50. 
#Beacuse in Python it first looks for Global variable and is so.
#It will give x =25 and scope the value of x=50 within that function

name ="This is a global name"

def name_func():
    name="Sammy"

    def print_name():
        print("tHE NAME IS:",name)

    print_name()

name_func()
print(name)

# For the function print_name; the name="sammy" 
# as the  function is present inside another function, 
# hence it will look outside first and then

y= 1000

def my_func1(y):
    print('The value of x is: ', y)
    y=100
    print('The value of is has changed to: ',y)

my_func1(y)
print(y)


## Change global value inside the functions

z = 90

def my_j():
    global z
    z=100

print("Before function call:",z)
my_j()
print("After function call:",z)

#Reassigning global value, inside a function 
# The better approach would have been to be done via return 

