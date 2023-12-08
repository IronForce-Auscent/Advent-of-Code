from itertools import cycle

class Part1():
    def __init__(self):
        self.instructions = None
        self.nodes = None

    def read_data(self):
        with open("input.txt", "r") as f:
            document = f.read()
        return document

    def execute_instructions(self):
        start_pos = [node for node in self.nodes if node.endswith("A")] # Get all nodes that end with the letter 'A"
        steps = [0] * len(start_pos) # Create a list of zeros for each starting node

        for i, node in enumerate(start_pos):
            """
            Generates a list containing 1's and 0's depending if the current instruction being parsed is a "R" or not, then
            passes the list through the cycle() function to generate an iterator
            """
            c = cycle(int(instruction == "R") for instruction in self.instructions)
            while not node.endswith("Z"):
                steps[i] += 1
                node = self.nodes[node][next(c)] # Gets the next node in the sequence, depending if the earlier instruction is to go right or left

        return start_pos, steps

    def main(self):
        self.instructions, _, *nodes = self.read_data().splitlines()
        self.nodes = {node[0:3]: (node[7:10], node[12:15]) for node in nodes}
        start_pos, steps = self.execute_instructions()
        print(start_pos)
        print(steps)
        print(steps[start_pos.index("AAA")])

if __name__ == "__main__":
    part1 = Part1()
    part1.main()