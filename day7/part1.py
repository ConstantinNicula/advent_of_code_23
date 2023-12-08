import sys
from enum import Enum

class HandType(Enum): 
    FIVE_OF_A_KIND = 0 
    FOUR_OF_A_KIND = 1 
    FULL_HOUSE = 2 
    THREE_OF_A_KIND = 3 
    TWO_PAIR = 4 
    ONE_PAIR = 5 
    HIGH_CARD = 6 

class Hand:

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

        self.hand_score = None 
        self.card_score = None 

        self.__compute_score(cards) 

    def __compute_score(self, cards: str): 
        card_freq = {}
        for card in cards:
            card_freq[card] = card_freq[card] + 1 if card in card_freq else 1  

        num_cards = sorted(card_freq.values(), reverse=True)
        #unique_cards, num_cards = zip(*sorted(card_freq.items(), key=lambda x: x[1], reverse=True))
        self.hand_score = self.__hand_score(num_cards).value
        self.card_score = self.__cards_only_score(cards)

    def __cards_only_score(self, cards: str):
        score_table = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
        return tuple(map(lambda x: score_table.index(x), cards)) 

    def __hand_score(self, card_freq: list[int]) -> HandType:
        if card_freq[0] == 5: 
            return HandType.FIVE_OF_A_KIND
        if card_freq[0] == 4:
            return HandType.FOUR_OF_A_KIND

        if card_freq[0] == 3:
            if card_freq[1] == 2:
                return HandType.FULL_HOUSE
            if card_freq[2] == 1:
                return HandType.THREE_OF_A_KIND

        if card_freq[0] == 2:
            if card_freq[1] == 2:
                return HandType.TWO_PAIR
            if card_freq[1] == 1: 
                return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def __lt__(self, other) -> bool:
        if self.hand_score < other.hand_score:
            return True 
        elif self.hand_score > other.hand_score:
            return False
        else: return self.card_score < other.card_score

    def __repr__(self): 
        return self.cards

def read_input():
    ret = []
    for line in sys.stdin:
        line = line.rstrip()
        cards, bid = line.split(' ')
        ret.append(Hand(cards, int(bid))) 
    return ret

def solve(hands: list[Hand]):
    hands.sort(reverse=True)
    ranked_score = sum(map(lambda elem: (elem[0]+1)*elem[1].bid, enumerate(hands)))
    print(ranked_score)

def main():
    hands = read_input()
    solve(hands)

if __name__  == "__main__":
    main()