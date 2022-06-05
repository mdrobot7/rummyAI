#Game
from cards import Deck
import term

class Game:
    p1cards = [] #the bot
    p2cards = []
    deckObj = None
    deck = []
    discard = []
    melds = [[]]

    p1score = 0
    p1HasDrawn = False
    p2score = 0
    p2HasDrawn = False

    dealer = 1
    p2IsReal = False

    def __init__(self, numdecks, p2IsReal):
        self.deckObj = Deck(numdecks)
        self.deck = self.deckObj.getCards()
        self.p2IsReal = p2IsReal

    def deal(self, numcards):
        for i in range(numcards*2):
            if(i % 2 == 0): self.p1cards.append(self.deck[0])
            else: self.p2cards.append(self.deck[0])
            self.deck.pop(0) #the card is dealt out, so remove it from the deck

    def meld(self, cards): #cards: a list of cards to be melded
        for i in range(len(cards) - 1):
            if cards[i][1:] != cards[i + 1][1:]: break #check for sets
        else:
            self.melds.append(cards)
            return True

        for i in range(len(cards) - 1):
            if cards[i][0] != cards[i + 1][0] or int(cards[i][1:]) != int(cards[i + 1][1:]) + 1: break #check for runs
        else:
            self.melds.append(cards)
            return True
        return False
    
    def layoff(self, card, targetMeld): #card: a single card to be laid off
        target = self.melds[targetMeld]
        for i in range(len(target) - 1):
            if target[i][0] != target[i + 1][0]: break #see if the target is a same-card meld
        else:
            if card[0] == target[0][0]:
                self.melds[targetMeld].append(card)
                return True
            else: return False
        
        #if it got through the for loop, it is guaranteed to be a run, because it is already a meld. no need to check.
        if card[0] == target[0][0]:
            if int(card[1:]) == int(target[0][1:]) - 1: self.melds[targetMeld].insert(0, card)
            elif int(card[1:]) == int(target[len(target) - 1][1:]) - 1: self.melds[targetMeld].append(card)
            else: return False
            return True
        return False
    
    def waitForInput(self, msg, failmsg, inputs): #loops infinitely until one of the inputs is inputted
        while True:
            i = input(msg)
            for a in inputs: #if the inputted value matches one of the inputs, break
                if i == str(a): return i
            if failmsg != None: print(failmsg)

    def getP1Move(self): #the bot
        pass

    def getP2Move(self): #the player
        if self.p2IsReal:
            term.clear()
            term.homePos()
            while True:
                for i, card in enumerate(self.p2cards):
                    term.write(self.deckObj.cardToString(card))
                    term.pos(i*7, 1)
                action = self.waitForInput("What would you like to do? (\'d\' for draw, \'c\' for discard, \'m\' for meld, \'l\' for lay off): ",
                                           None, ["d", "c", "m", "l"])
                if action == "d":
                    if not self.p2HasDrawn:
                        action = self.waitForInput("Deck [\'d\'] or discard pile [\'c\']? ", None, ["d", "c"])
                        if action == "d":
                            self.p2cards.append(self.deck[0])
                            self.deck.pop(0)
                        else:
                            self.p2cards.append(self.discard[0])
                            self.discard.pop(0)
                        self.p2HasDrawn = True
                elif action == "c":
                    action = self.waitForInput("Pick a card to discard, and enter it here. ", None, self.p2cards)
                    print("Your turn has ended.")
                    break
                elif action == "m":
                    while True:
                        currentMeld = []
                        while action != "end":
                            action = self.waitForInput("Type which cards you would like to meld, one at a time. Type \'end\' to end. ", 
                                                       None, self.p2cards.copy().append("end"))
                            currentMeld += action
                        if self.meld(currentMeld): break
                        else:
                            print("That meld is not valid.")
                            break
                elif action == 'l':
                    action = self.waitForInput("Type which card you would like to lay off. ",
                                               None, self.p2cards)
                    target = self.waitForInput("Type which meld you would like to lay off into. ", None, range(len(self.melds)))
                    if self.layoff(action, target):
                        print("That layoff works!")
                    else:
                        print("That layoff is not valid.")

    def run(self):
        while self.p1score < 100 and self.p2score < 100:
            self.deal(10) #the computer deals first, player gets first move. after that, winner deals next round
            self.discard.append(self.deck[0]) #set up first discard card
            self.deck.pop(0)
            if self.dealer != 1: self.getP1Move() #if the player deals, the bot moves first

            while True:
                if len(self.p1cards) == 0: break
                self.getP2Move() #the real player
                if len(self.p2cards) == 0: break
                self.getP1Move() #the bot
            
            if len(self.p1cards) == 0: #p1 wins
                for card in self.p2cards:
                    if int(card[1:]) > 10: self.p1score += 10
                    else: self.p1score += int(card[1:])
            else: #p2 wins
                for card in self.p1cards:
                    if int(card[1:]) > 10: self.p2score += 10
                    else: self.p2score += int(card[1:])

        if self.p1score > 100: return 1
        elif self.p2score > 100: return 2
        else: return 0


if __name__ == "__main__":
    term.clear()
    game = Game(1, True)
    game.run()