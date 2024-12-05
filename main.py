import random


values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return "Card(" + self.rank + " of " + self.suit + ")"

class Deck:
    def __init__(self):
        self.allCards = []
        for suit in suits:
            for rank in ranks:
                self.allCards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.allCards)

    def dealOne(self):
        return self.allCards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.allCards = []
    
    def removeOne(self):
        return self.allCards.pop(0)
    
    def addCards(self, newCards):
        if type(newCards) == type([]): # we are adding multiple cards
            self.allCards.extend(newCards)
        else:
            self.allCards.append(newCards) # a single card
    
    def __str__(self):
        return f"Player {self.name} has {len(self.allCards)} cards."



playerOne = Player("One")
playerTwo = Player("Two")

newDeck = Deck()
newDeck.shuffle()

for x in range(26):
    playerOne.addCards(newDeck.dealOne())
    playerTwo.addCards(newDeck.dealOne())

gameOn = True
roundNumber = 0

while gameOn:
    roundNumber += 1
    print(f"Round {roundNumber}")
    
    if len(playerOne.allCards) == 0:
        print("Player One, out of cards! Player Two wins!")
        gameOn = False
        break
    if len(playerTwo.allCards) == 0:
        print("Player Two, out of cards! Player One wins!")
        gameOn = False
        break
    
    # start new round
    
    playerOneCards = [] # the cards p1 will leave on the table
    playerOneCards.append(playerOne.removeOne())
    
    playerTwoCards = [] # same but p2
    playerTwoCards.append(playerTwo.removeOne())
    
    atWar = True
    while atWar:
        if playerOneCards[-1].value > playerTwoCards[-1].value:
            playerOne.addCards(playerOneCards)
            playerOne.addCards(playerTwoCards)
            atWar = False
            
        elif playerOneCards[-1].value < playerTwoCards[-1].value:
            playerTwo.addCards(playerOneCards)
            playerTwo.addCards(playerTwoCards)
            atWar = False

        else:
            print("WAR!")
            
            if len(playerOne.allCards) < 3:
                print("Player One unable to declare war")
                print("Player Two wins!")
                gameOn = False
                break
            elif len(playerTwo.allCards) < 3:
                print("Player Two unable to declare war")
                print("Player One wins!")
                gameOn = False
                break
            else:
                for num in range(3):
                    playerOneCards.append(playerOne.removeOne())
                    playerTwoCards.append(playerTwo.removeOne())
            