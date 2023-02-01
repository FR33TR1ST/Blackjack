import random
import os
suits = ("clubs ", " diamonds", " hearts", " spades")
ranks =('A', 'K', 'Q', 'J', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five',
         'Four', 'Three', 'Two')
values = {'A':11, 'K':10, 'Q':10, 'J':10, 'Ten':10, 'Nine':9, 'Eight':8, 
          'Seven':7, 'Six':6, 'Five':5, 'Four':4, 'Three':3, 'Two':2}
packs_of_cards = 4

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
        
class Deck:
    def __init__(self):
        
        self.all_cards = []
        for times in range(packs_of_cards):
            for suit in suits:
                for rank in ranks:
                    created_card = Card(suit,rank)
                    
                    self.all_cards.append(created_card)
    
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []
        
    def remove_one(self):
        return self.cards.pop(0)
        
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
new_deck = Deck()
new_deck.shuffle()
dealer = Player("Machine")
player1 = Player(input("How do u want to be called?: "))
game_on = True
answer = False
player_wins = 0
dealer_wins = 0

while game_on:
    for i in range(len(player1.cards)):
        player1.remove_one()
    for l in range(len(dealer.cards)):
        dealer.remove_one()
    answer = False
    for x in range(2):
        dealer.cards.append(new_deck.deal_one())
        player1.cards.append(new_deck.deal_one())
    result = player1.cards[0].value + player1.cards[1].value
    print(f"Your carts are: {player1.cards[0]} and {player1.cards[1]} and u have {result} points")
    answerA = False
    if player1.cards[0].value == 11:
        while answerA not in [1,11]:
            answerA = int(input("Ur A have the value of 1 or 11?: "))
        if answerA == 1:
                player1.cards[0].value = 1
    elif player1.cards[1].value == 11:
        while answerA not in [1,11]:
            answerA = int(input("Ur A have the value of 1 or 11?: "))
        if answerA == 1:
                player1.cards[1].value = 1
                
    while answer != "N":
        answer = False
        while answer not in ["Y", "N"]:
            answerA = False
            answer= input("Do u want ask for a card: Y or N: ").capitalize()
            if answer == "Y":
                new_card = new_deck.deal_one()
                print(f"Your card is {new_card}")
                if new_card.value == 11 and result + new_card.value > 21 :
                    new_card.value = 1
                elif new_card.value == 11 and result + new_card.value <= 21:
                    while answerA not in [1,11]:
                        try:
                            answerA = int(input("Ur A have the value of 1 or 11?: "))
                        except:
                            pass    
                        if answerA == 1:
                            new_card.value = 1
                player1.cards.append(new_card)
                result += player1.cards[-1].value
                
            elif answer == "N":
                print(f"Pass")

        if result < 21:
            print(f"Your points are {result}")
        elif result == 21:
            print("BLACK JACK!!!!!!!!!!!!!!!!!")
            answer = "N"
        elif result > 21:
            answer = "N"
    answer=False
    if result > 21:
        print("You lost!!! Loser!!!!!")
    elif result <= 21:
        result_mac = dealer.cards[0].value + dealer.cards[1].value
        print(f"The Machine cards are {dealer.cards[0]} and {dealer.cards[1]}")
        while result_mac < result and result_mac <= 21:
            print("The Machine ask for a card")
            new_card=new_deck.deal_one()
            if new_card.value == 11:
                if result_mac + new_card.value > 21:
                    new_card.value = 1
            dealer.cards.append(new_card)
            result_mac += dealer.cards[-1].value
            if result_mac > 21:
                print(f"The card dropped {dealer.cards[-1]}")
                print("Machine Lost")
            elif result_mac == 21:
                print("BLACK JACK!!!!!!!!!!!!!!!!!")

        print(f"Your points: {result}, Machine points:{result_mac}")
    if result > 21:
        result = 0
        result_mac = 1
    elif result_mac > 21:
        result_mac = 0
    if result > result_mac:
        print("You Win! Congrats")
        player_wins += 1
    elif result < result_mac:
        print("Machine Wins! Looser")
        dealer_wins += 1
    elif result == result_mac:
        print("TIE!!!")
    print(f"Your wins: {player_wins}, Machine wins: {dealer_wins}")
    while answer not in ["Y", "N"]:
        answer = input("Do you want continue? Y or N: ").capitalize()
        if answer == "N":
            game_on = False
            break
    if len(new_deck.all_cards) < 10:
        new_deck = Deck()
        new_deck.shuffle()