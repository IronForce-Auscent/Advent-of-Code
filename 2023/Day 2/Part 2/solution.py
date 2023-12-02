import re

class Part1():
    def __init__(self):
        self.cubes = {"red": 12, "green": 13, "blue": 14}
        self.instructions: dict | str | list = None
        self.powers = []

    def read_data(self):
        with open("testcases.txt", "r") as f:
            document = f.read()
        return document

    def modify_instructions(self):
        self.instructions = self.instructions.splitlines()
        tmp = {}
        for i in range(len(self.instructions)):
            self.instructions[i] = self.instructions[i].split(":")[1].strip()
            outcomes = self.instructions[i].split(";")
            tmp[i+1] = outcomes
        self.instructions = tmp
    
    def parse_outcomes(self, outcomes: list[str]):
        displays = []
        for outcome in outcomes:
            displays.extend(outcome.strip().split(","))
        return displays
    
    def calculate_power(self, game: int, outcomes: list[str]):
        # Input eg: 1 ['3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
        displays = self.parse_outcomes(outcomes)
        # displays eg: ['6 red', ' 1 blue', ' 3 green', '2 blue', ' 1 red', ' 2 green']
        power = [0, 0, 0] # red, green, blue respectively
        reference = ["red", "green", "blue"]
        for display in displays:
            quantity, color = display.split()
            if power[reference.index(color)] < int(quantity):
                power[reference.index(color)] = int(quantity)
        self.powers.append(power[0] * power[1] * power[2])

    def main(self):
        self.instructions = self.read_data()
        self.modify_instructions() 
        print(self.instructions)
        for game, outcomes in self.instructions.items():
            self.calculate_power(game, outcomes)
        print(self.powers)
        print(sum(self.powers))


if __name__ == "__main__":
    part1 = Part1()
    part1.main()


