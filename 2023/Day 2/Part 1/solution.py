import re

class Part1():
    def __init__(self):
        self.cubes = {"red": 12, "green": 13, "blue": 14}
        self.instructions: dict | str | list = None
        self.possible_games = []

    def read_data(self):
        with open("sample.txt", "r") as f:
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
    
    def identify_impossible_outcomes(self, game: int, outcomes: list[str]):
        # Input eg: 1 ['3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
        displays = self.parse_outcomes(outcomes)
        print(displays)
        for display in displays:
            _x = display.split()
            if int(_x[0]) > self.cubes[_x[1]]:
                return False
        self.possible_games.append(game)
        return True

    def main(self):
        self.instructions = self.read_data()
        self.modify_instructions() 
        print(self.instructions)
        for game, outcomes in self.instructions.items():
            print(game, outcomes)
            self.identify_impossible_outcomes(game, outcomes)
        print(self.possible_games)
        print(sum(self.possible_games))

if __name__ == "__main__":
    part1 = Part1()
    part1.main()


