import re

class Part1():
    def __init__(self):
        self.cards = []
        self.card_ids = []
        self.winning_numbers = []
        self.my_numbers = []
        self.scoresheet = []

    def read_data(self):
        with open("testcases.txt", "r") as f:
            self.cards.extend(f.read().split("\n"))
    
    def get_numbers(self):
        expr = r'\d+(?:\s+\d+)*|\d+(?:\s+\d+)*'
        for card in self.cards:
            numbers = re.findall(expr, card)
            # Numbers returns 3 items per card: the card number (or "ID"), the winning numbers and the numbers that you own
            self.card_ids.append(numbers[0])
            self.winning_numbers.append(numbers[1])
            self.my_numbers.append(numbers[2])
        
    def populate_scoresheet(self):
        self.scoresheet.extend([0 for _ in range(len(self.card_ids))])
    
    def get_scores(self):
        self.populate_scoresheet()
        for i in range(len(self.winning_numbers)):
            winning_numbers, my_numbers = self.winning_numbers[i].split(" "), self.my_numbers[i].split(" ")
            for number in my_numbers:
                if not number.isnumeric():
                    continue
                if number in winning_numbers:
                    if self.scoresheet[i] == 0:
                        self.scoresheet[i] = 1
                    else:
                        self.scoresheet[i] *= 2


    def main(self):
        self.read_data()
        self.get_numbers()
        self.get_scores()
        print(self.scoresheet)
        print(f"Sum of scores: {sum(self.scoresheet)}")

if __name__ == "__main__":
    part1 = Part1()
    part1.main()