#Cards

import random

#Unicode codes:
#Heart: U+2661
#Diamond: U+2662
#Spade: U+2664
#Club: U+2667

#   ♡♢♤♧

"""
 ___
| H |
| 10|
|___|
"""

class Deck:
    #Cards are stored with the following format: "D2" (2 of diamonds), "C13" (king of clubs), "H10" (10 of hearts)
    #Suit: H = heart, D = diamond, S = spade, C = club

    cards = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", 
             "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13",
             "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13",
             "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13"]
    
    heart = "♡"
    diamond = "♢"
    spade = "♤"
    club = "♧"

    def __init__(self, numdecks):
        self.cards = self.cards*numdecks #yes, this is allowed... sigh, python...
        self.cards = random.shuffle(self.cards)
    
    def shuffle(self, numtimes):
        for i in range(numtimes):
            self.cards = random.shuffle(self.cards)
        return self.cards
    
    def getCards(self):
        return self.cards
    
    def cardToString(self, card):
        suit = ""
        if card[0] == "H": suit = self.heart
        elif card[0] == "D": suit = self.diamond
        elif card[0] == "S": suit = self.spade
        elif card[0] == "C": suit = self.club
        else: return ""

        val = ""
        if card[1:] == "1": val = "A"
        elif card[1:] == "11": val = "J"
        elif card[1:] == "12": val = "Q"
        elif card[1:] == "13": val = "K"
        else: val = card[1:]

        return f"""
                 ___
                | {suit} |
                | {val}|
                |___|"""