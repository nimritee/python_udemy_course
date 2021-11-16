def cube1(x,y,z):
    return x+y ** z


list_1 = [1,2,3,4,5,6,7,8,9]
cubed = list(map(lambda x: pow(x,3), list_1))
print(cubed)