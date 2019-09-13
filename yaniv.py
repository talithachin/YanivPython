#Yaniv with 2 players 
#declare full deck, draw deck, discard deck, player 1 cards, player 2 cards
# draw function: draw Card from draw deck 
#discard function: allow player to choose the discard card and discard to the discard deck
#turns- indicate whose turn it is 
#error handling 
#count the player score on hand. 

from enum import Enum
from enum import IntEnum
import random
from pprint import pprint
import sys
 
# Card_suits = ['Clubs','Spades','Hearts','Diamonds']
# Faces = ['Jack','Queen','King']
# Special = ['Joker']
# Number_of_cards = [54]


class DeckOfCards():
    def __init__(self):
          
        face_cards = [Card(rank,suit) for rank in Faces for suit in Card_suits]
        self.deck_of_cards= regular_cards + face_cards
        print(self.deck_of_cards)

full_deck=[]
# draw_deck=[]
# discard_deck = []
# class Card(IntEnum):
#         'Ace'= 0  
#         '2'= 2
#         '3'= 3
#         '4' 4
#         '5': 5
#         '6': 6
#         '7': 7
#         '8': 8
#         '9': 9
#         '10': 10
#         'Jack': 10
#         'Queen': 10
#         'King': 10
#         'Joker':0
    
# class Suit(Enum):
#     SPADES = 'spades'
#     CLUBS = 'clubs'
#     HEARTS = 'hearts'
#     DIAMONDS = 'diamonds'

# class Card(object):
  
#     def __init__(self, suit, face, points):
#         self.suit = suit.capitalize()
#         self.face = face
#         self.points = points

#     def create_deck():
#         for suit in suit :
#             for card in card_values
#                 create_playingcard = PlayingCard(suit=suit, face=card_values.key(),points=card_values.values())
#                 full_deck.append(create_playingcard)
#     return full_deck 
# # def show_deck(self):


# def shuffle_deck(self):

#global variables 
# full_deck = []
# draw_deck= []
# discard_deck = []
# player1_cards = []
# player2_cards =[]
# ActivePlayer = 1

# # #card enum for playing cards 
# class Card(IntEnum):
#     ACE = 1 
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#     FIVE = 5
#     SIX = 6
#     SEVEN = 7
#     EIGHT = 8
#     NINE = 9
#     TEN = 10
#     JACK = 11
#     QUEEN = 12
#     KING = 13
  
# #suit enum for playing cards
# class Suit(Enum):
#     SPADES = 'spades'
#     CLUBS = 'clubs'
#     HEARTS = 'hearts'
#     DIAMONDS = 'diamonds'


# #class to hold info for playing cards 
# class PlayingCard:
#     def __init__(self,card_value,card_suit):
#         self.card = card_value
#         self.suit = card_suit

# #create a function to generate the full deck of card
# def create_deck():
#     for suit in Suit :
#         for card in Card:
#             create_card = card
#             create_suit = suit
#             create_playingcard = PlayingCard(card_value=create_card, card_suit=create_suit)
#             full_deck.append(create_playingcard)
#     return full_deck 

# #Draw Single Card from "deck"
# def draw_card(deck):
#     random_card= random.randint(0, len(deck)-1)
#     return deck.pop(random_card)

# def dealCards():
#     global player1_cards 
#     global player2_cards
#     if len(draw_deck) == len(full_deck):
#         for i in range (5):
#             player1_cards.append(draw_card(draw_deck))
#             player2_cards.append(draw_card(draw_deck))
#             # print ("player 1 cards are", player1_cards[i].card)
#     else:
#         print ("did not deal card")

# def turns():
#     global ActivePlayer
#     global player1_cards
#     global player2_cards 
#     if(ActivePlayer==1):
#         player1_cards.append(draw_card(draw_deck))
#         ActivePlayer=2  
#         print("Player 2")
#         # for x in range(0,len(player1_cards)):
#             # print(player1_cards[x].card, player1_cards[x].suit)
#     elif(ActivePlayer==2):
#         player2_cards.append(draw_card(draw_deck))
#         print("Player 1")
#         ActivePlayer=1
#     else :
#         print ("error")

# def discardCard():
#     dealCards()
#     turns()
#     if (ActivePlayer==1):
#         for i in range(0, len(player1_cards)):
#             print(player1_cards[i].card+ player1_cards[i].suit)
#             # print "[%s]" % ", '.join(map(str, player1_cardList))
#             # print('\n'.join(map(player1_cards[i].card, player1_cards[i].suit))) 
#             # print(card_chosen_player1)
#             # if card_chosen in player1_cards[i].card == True:
#     elif (ActivePlayer==2):
#         card_chosen_player2 = input("choose a card to discard out of your cards " )
#         for i in range(0, len(player2_cards)):
#             print(player2_cards[i].card,player2_cards[i].suit)
#             # print(card_chosen_player2)
#             # if card_chosen in player1_cards[i].card == Tru
#     else:
#         print("discardCard not working")


# create_deck()
# draw_deck = list(full_deck)
# discardCard()


# # for i in range(0, len(player1_cards)):
# #     if(player1_cards[i].card>player2_cards[i].card):
# #         print("Player 1 wins the hand with", player1_cards[i].card)
# #         print("Player2 loses with", player2_cards[i].card)
# #     if(player1_cards[i].card <player2_cards[i].card):
# #         print("Player 2 wins the hand with:",player2_cards[i].card)
# #         print("player 1 loses the h with", player1_cards[i].card)
# #     else:
# #         print("WARRRRRR")