from itertools import cycle
from math import lcm

class Part1():
    def __init__(self):
        self.instructions = None
        self.nodes = None

    def read_data(self):
        with open("input.txt", "r") as f:
            document = f.read()
        return document

    def execute_instructions(self):
        """
        For part 2, this code does significantly more compared to part 1

        In part 2, the key difference is that we must start on nodes that end with "A", and end on nodes that end with "Z". Hence, start_pos
        must contain all the nodes that end with "A", and steps must be populated with an equal number of 0's

        Afterwards, iterate through each start node and regenerate the generator function. Loop through each node, going down the instructed direction
        until you reach a node that ends with "Z", and move on to the next start node in the list.

        Once all the start nodes have been computed, return the list containing the number of steps taken from each start node to an end node, as well
        as the list of start nodes... just for good measures
        """
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
        """
        Honestly I don't quite understand this part myself at the time of writing this comment, so I'll try my best to explain it to
        other users (and future me).

        Apparently the reason why LCM works for this input (and possibly this input only) is because the number of nodes between the start
        node and a valid end node is the same as between that end node and another copy of itself down the chain somewhere. Had the length between cycles
        be different, LCM may not be possible for this challenge

        To illustrate with a modified sample (see sample.txt):

        Focusing on these two nodes in particular, 

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)

        With the given directions ("L", "R"), you would essentially be going in this cycle
        
        11A -- (L) --> 11B -- (R) --> 11Z -- (L) --> 11B -- (R) --> 11Z ...

        The problem is the same if you start at 22A
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)

        You would be going from 22A to 22B, to 22C, to 22Z, to 22B, to 22C and over and over again (once you reached 22B, it doesnt matter what
        instructions you got since you would always be stuck in an infinite loop)

        This entire challenge is, in essence, a highly-glorified "Trains A, B, C, D leave the train station at 0900 with speeds... What time will
        all 4 trains return to the train station together?". And hence why LCM works for this challenge

        TL;DR: LCM works because we assume regular cycles between end nodes (we assume the start node is an end node for this TL;DR)
        """
        print(lcm(*steps))

if __name__ == "__main__":
    part1 = Part1()
    part1.main()