from sample import Sample
from testcases import TestCases
import re

class CrateMover():
    def __init__(self):
        self.ship = TestCases()
        self.cargo_ship: list[list] = self.ship.cargo_ship
        self.instructions = self.ship.instructions.strip().split("\n")

    def evaluate_regex(self, instruction: str):
        re_expression = r'\d+'
        match = re.findall(re_expression, instruction)
        return match

    def move_crates(self, quantity: int, start: int, end: int):
        to_move = self.cargo_ship[start][len(self.cargo_ship[start]) - quantity: len(self.cargo_ship[start])]
        print(f"To move: {to_move}")
        self.cargo_ship[end].extend(to_move)
        del self.cargo_ship[start][len(self.cargo_ship[start]) - quantity: len(self.cargo_ship[start])]

    def evaluate(self):
        parsed_instructions = []
        for instruction in self.instructions:
            parsed_instructions.append(self.evaluate_regex(instruction))
        for instruction in parsed_instructions:
            print(f"{self.cargo_ship}    ({instruction})")
            self.move_crates(int(instruction[0]), int(instruction[1]), int(instruction[2]))
    
    def get_toplevel_crate(self):
        toplevel = ""
        for stack in self.cargo_ship:
            if stack != []:
                toplevel += stack[-1]
        return toplevel

def main():
    cratemover = CrateMover()
    cratemover.evaluate()
    print(cratemover.cargo_ship)
    print(cratemover.get_toplevel_crate())

if __name__ == "__main__":
    main()