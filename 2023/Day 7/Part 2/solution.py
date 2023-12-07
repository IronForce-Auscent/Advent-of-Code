from enum import Enum
import collections

class Card(int):
    """
    Represents card value. str to int conversion must be done using __new__ since Card() is a subclass of int(), which is immutable
    """
    def __new__(cls, val, jokers=False):
        if isinstance(val, str):
            if val == "T":
                val = 10
            elif val == "J":
                val = 1 if jokers else 11
            elif val == "Q":
                val = 12
            elif val == "K":
                val = 13
            elif val == "A":
                val = 14
            else:
                val = int(val)
        
        return super(cls, cls).__new__(cls, val)
    
    def __repr__(self):
        if self == 1:
            return "Joker"
        elif self <= 10:
            return int.__repr__(self)
        else:
            if self == 11:
                return "Jack"
            elif self == 12:
                return "Queen"
            elif self == 13:
                return "King"
            elif self == 14:
                return "Ace"
            else:
                raise Exception("How did we get here?")           


class Rankings(Enum):
    """
    Represents results of each hand, to allow for easy comparison. Sorted from highest to lowest
    """
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self == Rankings.FIVE_OF_A_KIND:
            return "five of a kind"
        elif self == Rankings.FOUR_OF_A_KIND:
            return "four of a kind"
        elif self == Rankings.FULL_HOUSE:
            return "full house"
        elif self == Rankings.THREE_OF_A_KIND:
            return "three of a kind"
        elif self == Rankings.TWO_PAIRS:
            return "two pairs"
        elif self == Rankings.ONE_PAIR:
            return "one pair"
        elif self == Rankings.HIGH_CARD:
            return "high card"
        
    def __int__(self):
        return self.value


class Part2():
    """
    Represents a hand of 5 cards, as well as properties to cache results of each hand and counts of values in the
    hand for easy reference
    """

    def __init__(self, cards, bid, jokers=False):
        self.cards = [Card(c, jokers) for c in cards]
        self._result = None
        self.val_counts = None
        self.bid = int(bid)
        self._use_jokers = jokers

    def __repr__(self):
        return self.cards
    
    def get_hand_result(self):
        # Cache the result
        if self._result is not None:
            return self._result
        
        # Check for multiples
        self.val_counts = collections.Counter(self.cards)

        has_five_of_a_kind = False
        has_four_of_a_kind = False
        has_three_of_a_kind = False
        pair_count, joker_count = 0, 0

        for val, count in self.val_counts.most_common():
            if self._use_jokers and val == 1:
                joker_count = count
            elif count == 5:
                has_five_of_a_kind = True
            elif count == 4:
                has_four_of_a_kind = True
            elif count == 3:
                has_three_of_a_kind = True
            elif count == 2:
                pair_count += 1
        
        if has_five_of_a_kind:
            self._result = Rankings.FIVE_OF_A_KIND

        elif has_four_of_a_kind:
            if joker_count == 1:
                self._result = Rankings.FIVE_OF_A_KIND
            else:
                self._result = Rankings.FOUR_OF_A_KIND

        elif has_three_of_a_kind:
            if pair_count > 0:
                self._result = Rankings.FULL_HOUSE
            elif joker_count == 2:
                self._result = Rankings.FIVE_OF_A_KIND
            elif joker_count == 1:
                self._result = Rankings.FOUR_OF_A_KIND
            else:
                self._result = Rankings.THREE_OF_A_KIND

        elif pair_count == 2:
            if joker_count == 1:
                self._result = Rankings.FULL_HOUSE
            else:
                self._result = Rankings.TWO_PAIRS

        elif pair_count == 1:
            if joker_count == 3:
                self._result = Rankings.FIVE_OF_A_KIND
            elif joker_count == 2:
                self._result = Rankings.FOUR_OF_A_KIND
            elif joker_count == 1:
                self._result = Rankings.THREE_OF_A_KIND
            else:
                self._result = Rankings.ONE_PAIR
        
        # No other possible matches, so either high card or jokers to make other matches
        elif joker_count in (4, 5):
            self._result = Rankings.FIVE_OF_A_KIND
        elif joker_count == 3:
            self._result = Rankings.FOUR_OF_A_KIND
        elif joker_count == 2:
            self._result = Rankings.THREE_OF_A_KIND
        elif joker_count == 1:
            self._result = Rankings.ONE_PAIR
        else:
            self._result = Rankings.HIGH_CARD

        return self._result

    def has_higher_card(self, other):
        """
        Use this to break ties between cards of similar rankings, check sequential order
        """
        # Since both cards have the same results, then we just need to check the card with the highest score
        for i in range(5):
            if self.cards[i] > other.cards[i]:
                return True
            elif other.cards[i] > self.cards[i]:
                return False
            
        # Just in case of absolute tie, return true
        return True 
    
    def beats_hand(self, other):
        """
        Get hand results first, if they are not equal then we can use those results, otherwise we
        check the highest card
        """
        result_self = self.get_hand_result()
        result_other = other.get_hand_result()

        if result_self == result_other:
            res = self.has_higher_card(other)
        else:
            print(result_self)
            print(result_other)
            res = result_self.value > result_other.value
        return res
    
    def __lt__(self, other):
        """
        Implement __lt__ so we can use sorted operation

        ... yeah I don't know what that means either, I just copied it :P
        """
        return self.beats_hand(other)

def read_data():
    with open("input.txt", "r") as f:
        document = f.read()
    return document

def parse_data(data: list[str]):
    hands, bets = [], []
    for entry in data:
        hand, bet = entry.split()
        hands.append(hand)
        bets.append(bet)
    return hands, bets

def main():
    data = read_data().split("\n")
    card_sets, bets = parse_data(data)
    hands = []
    total = 0
    for card_set, bet in zip(card_sets, bets):
        hand = Part2(card_set, bet, jokers=True)
        hands.append(hand)
    
    # Sort all the hands
    for rank, hand in enumerate(sorted(hands, reverse=True), 1):
        total += rank * hand.bid
    print(total)

if __name__ == "__main__":
    main()