#List 

mylist = ['a','b','c']
mylist1 = ['1','a',1,1,True,7.9,3, [1,2,3]]
print(type(mylist1))
print(len(mylist1))

#Indexing 

mylist2 = [1,2,3,4,5,6]
print(mylist2[1])
print(mylist2[-1])

#Slicing 

print(mylist2[2:])
print(mylist2[:5])
print(mylist2[::2])

#List are mutable 
mylist2[0] = 'Hello'
print(mylist2)

#Basic Fuctions

#Adding elements to the list
mylist2.append('hello')
print(mylist2)

mylist3 = [1,4,5,6]
mylist2.append(mylist3)
print(mylist2)
mylist2.extend(mylist3)
print(mylist2)

#Removing elements from the list 

e = mylist.pop()
print(mylist)
print(e)

mylist.pop(0)
print(mylist)

#Reverse the list 

mylist1.reverse()
print(mylist1)

#Sort the list 

mylistnum = [6,23,22,1,2,3]
mylistnum.sort()
print(mylistnum)

#Indexing list inside list
mylistindex = [1,2,['x','y','z']]
print(mylistindex[2][1])