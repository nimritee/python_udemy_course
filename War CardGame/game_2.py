
# War card game, between 2 people. You and the Computer.

# Basic Rules 
#The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first.
# Each player faces his stack of cards face down, in front of him.

#The Play

#Each player turns up a card, the player with the higher card, takes both the cards, face down, on bottom of his stack.
#If the cards are of the same rank, it is war! Each player turns up three cards face down and one card face up. 
# The player with the higher card, takes both the piles (6 cards). If the turned up cards are agaian the same rank, 
# each player places another card face down and turns another card face up. The player with the higher card takes all the 10 cards and so on.

import random
import itertools

SUITE = 'H S D C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():

    def __init__(self):
        print("Creating New Ordered Deck!")
        self.allcards = list(itertools.product(RANKS,SUITE))
    
    def shuffle_card(self):
       print("Shuffling Deck")
       random.shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])


class Hand():
    
    def __init__(self,cards):
        self.cards = cards
    
    def __str__(self): #Will tell me how many cards the player has in his hand
        return "Contains {} card",format(len(self.cards))
    
    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player():
    
    def __init__(self,name,hand):
        self.name =name
        self.hand =hand
    
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {} \n".format(self.name,drawn_card))
        return drawn_card
    
    def remove_war_card(self):
        war_card =[]
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_card.append(self.hand.remove_card())
            return war_card
    
    def still_has_cards(self):
        return len(self.hand.cards) != 0

name = input("Hallo, what is your Name: ")
print("Welcome to the War! {}".format(name))

d = Deck()
d.shuffle_card()
half1,half2 = d.split_in_half()

comp = Player("computer",Hand(half1))
user = Player(name,Hand(half2))

total_rounds = 0
war_count =0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("Time for a new round!")
    print("Here are current standing:")
    print(user.name+" has the count:" + str(len(user.hand.cards)))
    print("Computer has the count:" + str(len(user.hand.cards)))
    print("Play a card!\n")

table_card=[]

c_card = comp.play_card()
p_card =user.play_card()

table_card.append(c_card)
table_card.append(p_card)

if c_card[1] == p_card[1]:
    war_count +=1
    print("war")
    table_card.extend(user.remove_war_card())
    table_card.extend(comp.remove_war_card())

    if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
        user.hand.add(table_card)
    else:
        comp.hand.add(table_card)
else:
    if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
        user.hand.add(table_card)
    else:
        comp.hand.add(table_card)

print("Game Over,nos of rounds",total_rounds)
print("A war happend",war_count,"times")
