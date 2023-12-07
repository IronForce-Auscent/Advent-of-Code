from enum import Enum
import collections

class Rankings():
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Part1():
    def __init__(self):
        self.rankings = []
        self.strength = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

    def read_data(self):
        with open("input.txt", "r") as f:
            document = f.read()
        return document

    def parse_data(self, data: list[str]):
        hands, bets = [], []
        for entry in data:
            hand, bet = entry.split()
            hands.append(hand)
            bets.append(bet)
        return hands, bets

    def calculate_scores(self, hand_bets: list):
        hand = hand_bets[0]
        ranking = self.calculate_rankings(hand)
        return [ranking] + [self.strength[card] for card in hand]

    
    def calculate_total_winnings(self, hand_bets: list):
        """
        Working as intended
        """
        in_order = sorted(hand_bets, key=self.calculate_scores)
        winnings, rank = 0, 1
        for _, bid in in_order:
            winnings += bid * rank
            rank += 1
        return winnings

    def main(self):
        data = self.read_data().split("\n")
        hands, bets = self.parse_data(data)
        hand_bets = []
        for i in range(len(bets)):
            hand = hands[i]
            hand_bets.append((hand, int(bets[i])))
        winnings = self.calculate_total_winnings(hand_bets)
        print(winnings)


        """self.sort_by_types(hands)
        print(self.types)
        self.calculate_rankings()"""

if __name__ == "__main__":
    part1 = Part1()
    part1.main()