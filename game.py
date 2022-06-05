#Game
import random
import term

class Game:
    deck = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", 
             "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13",
             "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13",
             "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13"]
    p1cards = [] #the bot
    p2cards = []
    discard = []

    p2IsReal = False
    numcards = 0

    def __init__(self, numdecks = 1, numcards = 5, p2IsReal = False):
        self.deck = self.deck*numdecks
        for i in range(5): random.shuffle(self.deck) #shuffle 5 times, just because
        self.p2IsReal = p2IsReal
        self.numcards = numcards
    
    def deal(self):
        for i in range(0, self.numcards*2, 2):
            self.p1cards.append(self.deck[0])
            self.p2cards.append(self.deck[1])
            self.deck.pop(0)
            self.deck.pop(0)
        self.discard.append(self.deck[0])
        self.deck.pop(0)

    def checkHand(self, hand):
        isSet = True
        isSetWrongCard = False
        isRun = True
        isRunWrongCard = False
        for i in range(len(hand) - 1):
            if hand[i][0] != hand[i + 1][0]: isSetWrongCard = True #these ifs allow for ONE wrong card in a hand of x cards (usually 5)
            if int(hand[i][1:]) != int(hand[i + 1][1:]) + 1: isRunWrongCard = True

            if hand[i][0] != hand[i + 1][0] and isSetWrongCard: isSet = False
            if int(hand[i][1:]) != int(hand[i + 1][1:]) + 1 and isRunWrongCard: isRun = False
        if isSet or isRun: return True
        else: return False

    def waitForInput(self, prompt, inputs):
        while True:
            i = input(prompt)
            for ins in inputs:
                if i == ins: return i

    def takeInput(self, player):
        if player == 1: cards = self.p1cards
        elif player == 2: cards = self.p2cards
        else: return
        print(cards)
        
        print("Top card of the discard pile: " + self.discard[0])
        play = self.waitForInput("Do you want to draw from the deck or the discard pile? [d, p] ", ["d", "p"])
        if play == "d":
            cards.append(self.deck[0]) #add the card from the deck
            self.deck.pop(0)
        else:
            cards.append(self.discard[0]) #add the card from the discard pile
            self.discard.pop(0)
        
        print("\n\n")
        print(cards)
        discard = self.waitForInput("Which card would you like to discard? ", cards)
        self.discard.insert(0, discard) #put the discarded card in the 0 slot of the discard list
        cards.remove(discard)
        if player == 1: self.p1cards = cards
        else: self.p2cards = cards

    def run(self):
        self.deal()
        while True:
            print("\nPlayer 1: ")
            self.takeInput(1)
            if self.checkHand(self.p1cards): return 1
            print("\nPlayer 2: ")
            self.takeInput(2)
            if self.checkHand(self.p2cards): return 2

if __name__ == "__main__":
    game = Game(1, 5, True)
    print(game.run())