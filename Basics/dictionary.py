my_stuff = {"key1": "alue", "key2": "value3"}
diction1 = {
    "fast": "to move quickly",
    "harry": "a coder",
    "numbersw": [1, 2, 5],
    "anotherdic": {"superfast": "extremequick"},
    1: 2,
}
print(my_stuff['key2'])
print(diction1['anotherdic']['superfast'])
diction1['nimrite'] = '8'
print(diction1)


#Tuple
tuple2 = (1,3,4)
print(tuple2[0])

#Set 

x= set()
x.add(1)
x.add(1)
x.add(1)

print(x) # Will add only unique elemets

y = set([8,2,3])
print(y)