import re

class Part1():
    def __init__(self):
        self.cards = []
        self.card_dict = {}
        self.scoresheet = {}
        self.inventory = {}

    def read_data(self):
        with open("testcases.txt", "r") as f:
            self.cards.extend(f.read().split("\n"))
    
    def process_cards(self):
        expr = r'\d+(?:\s+\d+)*|\d+(?:\s+\d+)*'
        for card in self.cards:
            numbers = re.findall(expr, card)
            # Numbers returns 3 items per card: the card number (or "ID"), the winning numbers and the numbers that you own
            win_no = [num for num in numbers[1].split()]
            my_no = [num for num in numbers[2].split()]
            self.card_dict[numbers[0]] = [win_no, my_no]
            self.inventory[numbers[0]] = 1

    def get_cards_won(self):
        for id, numbers in self.card_dict.items():
            self.scoresheet[id] = 0
            win, own = numbers[0], numbers[1]
            for num in own:
                if num in win:
                    self.scoresheet[id] += 1
        
        for id, count in self.scoresheet.items():
            for i in range(1, count + 1):
                x = str(int(id) + i)
                self.inventory[x] += self.inventory[id]
            

    def main(self):
        self.read_data()
        self.process_cards()
        self.get_cards_won()
        print(self.scoresheet)
        print(self.inventory)
        print(sum(self.inventory.values()))

if __name__ == "__main__":
    part1 = Part1()
    part1.main()