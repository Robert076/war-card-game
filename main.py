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


newDeck = Deck()
newDeck.shuffle()
for card in newDeck.allCards:
    print(card)

newPlayer = Player('Jose')
print(newPlayer)
newPlayer.addCards(newDeck.dealOne())
print(newPlayer)