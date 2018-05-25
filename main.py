#warning: this game uses random draws from the stack of the player instead of using sequential draws, as in normal war.

import random

cards = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king','ace','2','3','4','5','6','7','8','9','10','jack','queen','king','ace','2','3','4','5','6','7','8','9','10','jack','queen','king','ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

value_cards = {'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':11,'queen':12,'king':13,'ace':14}

player1cards = []
player2cards = []

n = 1
while len(cards) > 0:
    card = random.choice(cards)
    if n%2 == 0:
        player1cards.append(card)
    else:
        player2cards.append(card)
    cards.remove(card)
    n+=1

player1 = input('player 1 name: ')
player2 = input('player 2 name: ')

print(player1, " has the cards ", player1cards)
print(player2, " has the cards ", player2cards)

def war(cardsused1, cardsused2):
    try:
        newcard1 = random.choice([x for x in player1cards if x not in cardsused1])
        newcard2 = random.choice([x for x in player2cards if x not in cardsused2])
        print('war! cards pulled: ', newcard1, newcard2)
        cardsused1.append(newcard1)
        cardsused2.append(newcard2)
        if value_cards[newcard1] > value_cards[newcard2]:
            for i in cardsused2:
                player1cards.append(i)
                player2cards.remove(i)
            print(player1, ' has won the cards ', cardsused2)
        elif value_cards[newcard1] < value_cards [newcard2]:
            for i in cardsused1:
                player1cards.remove(i)
                player2cards.append(i)
            print(player2, ' has won the cards ', cardsused1)
        else:
            war(cardsused1,cardsused2)
    except IndexError:#for when no more cards
        if len([x for x in player1cards if x not in cardsused1]) == 0:
            for i in cardsused1:
                player1cards.remove(i)
                player2cards.append(i)
        else:
            for i in cardsused2:
                player1cards.append(i)
                player2cards.remove(i)

#play
while len(player1cards) > 0 and len(player2cards) > 0:
    card1 = random.choice(player1cards)
    card2 = random.choice(player2cards)
    print('cards pulled: ', card1, card2)
    if value_cards[card1] > value_cards[card2]:
        player1cards.append(card2)
        player2cards.remove(card2)
        print(player1, ' has won the card ', card2)
    elif value_cards[card1] < value_cards [card2]:
        player1cards.remove(card1)
        player2cards.append(card1)
        print(player2, ' has won the card ', card1) 
    else:
        war([card1], [card2])

#finish
if len(player1cards) == 0:
    print(player2, 'has won!')
else:
    print(player1, 'has won!')
