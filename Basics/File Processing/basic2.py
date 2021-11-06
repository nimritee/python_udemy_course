import time
import os

while True:
    if os.path.exists("fruits.txt"):
        with open("fruits.txt") as myfile:
            print(myfile.read())
    else:
        print("The file does not exists")
    time.sleep(10)