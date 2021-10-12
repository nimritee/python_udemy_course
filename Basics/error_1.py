try:
    f = open('s1.txt','r')
    f.write('I am writing in the file!')
except IOError:
    print("I am in IO Error")
else:
    print("success")
    f.close()
finally:
    print("I always work no matter what!")
print("Hello World")    