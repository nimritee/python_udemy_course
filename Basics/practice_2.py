# Problem 1 

#Given a list of Integers, return true if the sequnence of numbers 1,2,3 appear in the list somewhere 

#For example
#arrayCheck([1,1,2,3,1]) -> True
#arrayCheck([1,1,2,4,1]) -> False
#arrayCheck([1,1,2,1,2,1,2,3]) -> True

# 1. Take the list from the user 
# 2. Iterate through the list and find if the numbers given are present or not.

#Solution

#****************************************************#
# count = int(input("How many numbers to be taken: "))
# new_list =[]
# if type(count) == type(10):
#     for num in range(count):
#         new_list.append(int(input('Enter the number: ')))
# else:
#     print("Please pass a valid number")

# counter = True
# print(new_list)
# given_numbers  = [1,2,3]
# for item in given_numbers:
#     value = item in new_list
#     if value == False:
#         counter = False

# if counter == True:
#     print('The number is present in the list')
# else:
#     print('The number is not present in the list')

#****************************************************#


#Problem 2 

#Given a string, return a new string made of every other character starting with first; so Hello -> 'Hlo'

#Example
#Hello -> Hlo 
#Hi -> H
#Heeololeo -> Hello

#Solution

#****************************************************#

# def step_string(user_string):
#     return user_string[::2]

# user_string = input("Enter the string to be transfomed: ")
# result = step_string(user_string)
# print(result)

#****************************************************#


#Problem 3 

#Given two strings, return TRUE if either of the strings appear at the very end of the other string, ignoring upper/lower case differences 

#('anc','yanc') ->True 
#('hellooo','ooo') ->True 

# 1. Accept two strings from the users; making them to lowercase
# 2. Get the length of both the strings 
# 3. Take the smaller one 3
# 4. Take that length of the larger string;  (4:)  (Length of larger String - Smaller)
# 5. and then check if its equal 


#Solution

#****************************************************#

# def accept_string():
#     return input('Please enter the value: ').lower()

# def small_string_func(len1,len2,string1,string2):
#     if len1 > len2:
#         return string2
#     elif len1 < len2:
#         return string1
#     else:
#         return 0

# def large_string_func(small_string,string1,string2,len1,len2):
#     if small_string == string1:
#         large_string_num = len2 - len1
#     else:
#         large_string_num = len1 - len2

#     if small_string == string1:
#         large_string = string2[large_string_num:]
#     else:
#         large_string = string1[large_string_num:]
#     return large_string

# string1 = accept_string()
# string2 = accept_string()

# len1 = len(string1)
# len2 = len(string2)

# small_string = small_string_func(len1,len2,string1,string2)
# if type(small_string) == type(10):
#     large_string = string2
# else:
#     large_string = large_string_func(small_string,string1,string2,len1,len2)
#     print(large_string)

# result = large_string == small_string
# print('The output of the strings is: ', result)

#****************************************************#

#Problem 4 

#Given a string, return a string where for every char in the original, there are two chars

#The = TThhee
#AAbb = AAAAbbbb

#Solution

#****************************************************#

# def double_string(user_string):
#     new_string =""
#     for item in user_string:
#         new_string = new_string+ item+item

#     return new_string

# user_string =input('Enter the string: ')
# output = double_string(user_string)
# print(output)

#****************************************************#

#Problem 5

# You will be given three integer, you need to find the sum of them, but all values from 13 - 19 have value = 0; except 15 and 16.

# 1. Take the three values from the user 
# 2. Find if the value is a teen value; if so what will be its value
# 3. Add all the number 

#Solution

#****************************************************#

# def accept_num():
#     return  int(input('Enter the number to be added: '))

# def get_value(num):
#     if num in range(13, 20):
#         if num in [15,16]:
#             value = num
#         else:
#             num = 0
#     else:
#         value = num
#     return num


# num1 = accept_num()
# num2 = accept_num()
# num3 = accept_num()

# sum = get_value(num1) + get_value(num2) + get_value(num3)
# print('The sum is: {}'.format(sum))

#****************************************************#


#Problem 6 

#Return the number of even integer in the given array

def accept_list(count):
    new_list =[]
    for item in range(count):
        new_list.append(int(input('The value is: ')))

    return new_list

count = int(input('The length of the array is: '))
new_list = accept_list(count)

even_num = filter(lambda num: num % 2 == 0,new_list)
even_num = len(list(even_num))
print('The count of even number is: {}'.format(even_num))

#****************************************************#