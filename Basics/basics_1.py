#Test 1 

#Given the string 

s= 'django'

print(s[0])
print(s[-1])
#djan
print(s[:4])
#jan
print(s[1:4])
#go
print(s[4:])


#Problem 2 

glist = [3,7,[1,4,'hello']]

#Reassign hello to be goodbye

glist[2][2] ="goodbye"
print(glist)

#Problem 3

d1 ={'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 ={'k1':[{'nest_key':['ths is',"hello"]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1])

#Problem 4 

mylist = [1,1,1,1,2,2,2,3,3,3,]
convert = set(mylist)
print(convert)


#Problem 5 

age = 4
name ="Sammy"

statement ="Hello my dog's name is {name} and he is {age} years old".format(name='Sammy',age=4)
print(statement)