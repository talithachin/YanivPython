
import random
from playsound import playsound

ActivePlayer=1
p2=[]
discard_deck=[]

class Card(object):
    def __init__(self,suit,val,points,rank):
        self.suit= suit
        self.value = val
        self.points = points
        self.rank = rank

    def show(self):
        print ("*** {} {} ***".format(self.value,self.suit))

    def __repr__(self):
        return "%s %s" % (self.value, self.suit)
    
    def __str__(self):
        return ("{} {}".format(self.value,self.suit))

    def byPoints_key(self, points):
        return self.points
    
    def __lt__(self, other):
        return self.rank < other.rank

class DrawDeck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suitType in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:      
                if value in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    points = int(value)
                    rank = int(value)
                elif value=="Ace":
                    points =int(1)
                    rank = 1
                elif value == "Jack": 
                    points = int(10)
                    rank = 11 
                elif value == "Queen": 
                    points = int(10)
                    rank = 12
                elif value == "King": 
                    points = int(10)
                    rank = 13
                self.cards.append(Card(suitType,value,points,rank) )
        # self.cards.append(Card("","Joker", int("0"), 0))
        # self.cards.append(Card("","Joker", int("0"), 0))
            
       
    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range((len(self.cards)-1),-1,-1):
            rand = random.randint(0,i)
            self.cards[i],self.cards[rand] = self.cards[rand],self.cards[i]

    def drawCard(self):
        print ("*** Card drawn: {} {} ***".format(self.cards[len(self.cards)-1].value,self.cards[len(self.cards)-1].suit))
        return self.cards.pop()
    
class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand=[]

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        playsound('dealingcards.wav')

    def startGame(self,deck):
        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())
    
    def sortMyHand (self):
        self.hand = sorted(self.hand)
        
    def showHand(self):
        for card in self.hand:
            card.show()
 
    def discard(self):
        discardNumber = raw_input("\nChoose [1] to discard a Single Card, [2] to discard cards of same value e.g. 8 Hearts, 8 Spades, [3] to discard consecutive cards e.g. Jack Hearts, Queen Hearts, King Hearts:     ")
        if discardNumber == "1": 
            chooseCard = raw_input('\nDISCARD: Type card name to discard, e.g. "King Hearts"    ' )
            for i in range(len(self.hand)):
                if (str(chooseCard.lower().strip()) == 
                (self.hand[i].value.lower() + ' ' + self.hand[i].suit.lower())) or (chooseCard.lower() == (self.hand[i].value.lower() + self.hand[i].suit.lower())):
                    playsound('dealingcards.wav')
                    discard_deck.append(self.hand.pop(int(i)))
                    print("\nDISCARD DECK:{}".format(discard_deck[len(discard_deck)-1]))
                    break
                else:
                    pass
        elif "2" in str(discardNumber):
            chooseCard1 = raw_input('\nDISCARD: card VALUE to discard, e.g. "2", "Ace"      ')
            for i in range (len(self.hand)-1,-1, -1): 
                if str(chooseCard1).lower().strip() in str(self.hand[i].value).lower(): 
                    print("DISCARDED: {} ".format(self.hand[i]))
                    discard_deck.append(self.hand.pop(int(i)))
                    playsound('doublecard.wav')
                else:
                    pass   
        elif "3" in str(discardNumber):  
            self.hand.sort()
            print(self.hand)
            for i in range(len(self.hand)-1,2,-1): 
                if self.hand[i].rank == self.hand[i-1].rank+1 == self.hand[i-2].rank+2:
                    discardMultiple = raw_input("\nDISCARD: Do you want to discard {}, {}, {} ? \n[Y] for Yes or [N] for No \n".format(self.hand[i-2], self.hand[i-1], self.hand[i]))
                    if discardMultiple == "y" or "yes":
                        playsound('triplecard.wav')
                        print("\nDISCARDED: {}, {}, {} ".format(self.hand[i-2], self.hand[i-1], self.hand[i]))
                        discard_deck.append(self.hand.pop(i))
                        discard_deck.append (self.hand.pop(i-1))
                        discard_deck.append(self.hand.pop(i-2))
                        break
                    elif "n" in discardMultiple:
                        pass
                    else:
                        pass
        else: 
                            pass
        
    
    def calcPoints(self):
        totalPoints=0
        for i in range(0,len(self.hand)):
            totalPoints += int(self.hand[i].points)
        print("POINTS = {}".format(totalPoints))

        if (totalPoints <=15)== True:
            declareWinner = raw_input("call Yaniv? (Y/N)")
            if "Y" or "Yes" in declareWinner.lower():
                print("YANIV!")
                playsound('LevelWin.wav')
            else:
                pass
        else:    
            pass
 
# START THE GAME HERE
drawdeck = DrawDeck()
drawdeck.shuffle()
playerNumber = input("enter number of players between 2-4 ")
playersList = []

if int(playerNumber)<5:
    for i in range(0, int(playerNumber)):
        print ("---------------------Player{} Starts Game---------------------".format(i+1))
        playersList.append(Player ("p{i}"))
        playersList[i].startGame(drawdeck)
        playsound('dealingcards.wav')
else: 
        print("Choose again. your playerNumber should be between 2-4")

        

while True:
    # GAME FINALLY BEGINS
    for i in range(0, int(playerNumber)):
        print("---------------------PLAYER{}'S TURN---------------------".format(i+1))
        playersList[i].showHand()
        print ("--------------------------------------------------------")
        if (len(discard_deck)) >0 and len(discard_deck)<30: 
            print("\nTOP OF DISCARD DECK:{} {} ".format(discard_deck[len(discard_deck)-1].value, discard_deck[len(discard_deck)-1].suit))
            chooseDeck = raw_input("\nDRAW: pick up from Discard Deck [1] or pick up from Draw Pile [2] :  " )
            if "1" in chooseDeck.lower():
                print('\n*** Card Drawn: {} ***'.format(discard_deck[len(discard_deck)-1]))
                playersList[i].hand.append(discard_deck[len(discard_deck)-1])
                playersList[i].discard()
                playersList[i].calcPoints()     
            elif "2" in chooseDeck.lower():
                playersList[i].draw(drawdeck)
                playersList[i].discard()
                playersList[i].calcPoints()
            else:
                print("Your input is not valid")
        elif (len(discard_deck))>=30:
            print("\nTOP OF DISCARD DECK:{}{}".format(discard_deck[len(discard_deck)-1].value, discard_deck[len(discard_deck)-1].suit))
            chooseDeck = raw_input("\nDRAW: pick up from Discard Deck [1] or pick up from Draw Pile [2]" )
            for i in range((len(discard_deck)-1)):
                drawdeck.cards.append(discard_deck[i])
                drawdeck.shuffle()
        else: 
            playersList[i].draw(drawdeck)
            playersList[i].discard()
            playersList[i].calcPoints()

         

# deck = DrawDeck()
# talitha = Player("Talitha")
# talitha.startGame(deck)
# talitha.sortMyHand()
# talitha.discard()
# talitha.showHand()



#             #     if discardMultiple.lower() == "y" or "yes":
            #         print('DISCARDED : {}, {}, {}'.format(self.hand[i], self.hand[i+1], self.hand[i+2]))
            #         discard_deck.append(self.hand.pop(i))
            #         discard_deck.append(self.hand.pop(i))
            #         discard_deck.append(self.hand.pop(i))     