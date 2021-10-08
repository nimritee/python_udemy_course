#########################################
# A simple Code Breaker Game #

# Nope  - All digits are wrong 
# Very Close - If two digits match
# Match - A digit matches
# CodeBroken - In case of a full Match

###########################################


# 1. Take the 3 digit  number from the user 
# 2. Check if the two numbers are same; if so return true - CodeBroken

# 2. Check if the first place matches ; result  - [0]
# 3. Check if the seconds place matches;  result - [0,1]

# 4. If the result array is:
#     Empty  - Nope
#     One Element  - Place and Value to be mentioned  - Match 
#     Two Element  - Two Elemnets place and value to be returned -  Very Close


####################     Solution     #######################

import random

def accept_num():
    user_number = int(input("Enter the Three Digit Number: "))
    if user_number in range(000,1000):
        return user_number
    else:
        return ("Please enter a valid input!")

def random_num():
    random_num = random.randint(000, 1000)
    print(random_num)
    return random_num

def match_number(user_number, random_num):
    result = {}
    random_num_list = []
    user_num_list =[]
    # position_couter = 0
    for x in str(user_number):
        user_num_list.append(x)

    for y in str(random_num):
        random_num_list.append(y)
        
    for position_couter,item in enumerate(user_num_list):
        item = str(item) 
        position = str(random_num).find(item)
        if position != -1:
            if user_num_list[position] == random_num_list[position]:
                position_indication = "{} position".format(position_couter)
                result[position_indication] = item

        # position_couter = position_couter +1
    return result

def guess_game(user_number,random_num):
    game_status = False
    if type(user_number) != type(10):
        print(user_number)
    elif user_number == random_num:
        print("Congratulations CodeBroken! {} is the Number :)".format(user_number))
        game_status = True
    else:
        match_count = match_number(user_number, random_num)
        if len(match_count) == 2:
            print("Very Colse")
            print("Status",(match_count))
        elif len(match_count) == 1:
            print("Match")
            print("Status",(match_count))
        else:
            print("No Match")
        print("Try Again!")
        print("***************************************")
    return game_status

    
def play_game(user_number,random_num):
    game_status = guess_game(user_number,random_num)
    if game_status == False:
        user_number = accept_num()
        game_status = play_game(user_number,random_num)
    else:
        print("Game Over")


print("Hallo")
user_name = input("Please Enter your Name: ")
print("***************************************")
print("Hello {} Welcome to CodeBreaker!".format(user_name))
print("The Number has been generated! ")
print("Let's see, if you can guess :)")
print("***************************************")

random_num = random_num()
user_number = accept_num()
game_over = play_game(user_number,random_num)