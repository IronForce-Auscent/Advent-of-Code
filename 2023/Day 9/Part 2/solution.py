from collections import Counter
import numpy

class Solver():
    def __init__(self):
        pass

    def read_data(self):
        with open("input.txt", "r") as f:
            document = f.read().splitlines()
        return document
    
    def get_difference(self, reading: list[int]):
        return numpy.diff(reading)
    
    def extrapolate_difference(self, reading: list[int]) -> int:
        differences = []
        difference = self.get_difference(reading)
        c = Counter(difference)
        flag = True
        while flag:
            if len(c) == 1 and c.most_common(1)[0][0] == 0:
                flag = False   
            differences.append(list(difference))
            difference = self.get_difference(difference)
            c = Counter(difference)
        
        new_value = 0
        for i in range(len(differences) - 1, 0, -1):
            new_value = differences[i - 1][0] - new_value
        return reading[0] - new_value
        

    def main(self):
        readings = self.read_data()
        value = 0
        for reading in readings:
            reading = list(map(int, reading.split()))
            new_value = self.extrapolate_difference(reading)
            value += new_value
            print(f"New value for reading {reading}: {new_value}")
        print(f"Final value: {value}")

if __name__ == "__main__":
    solver = Solver()
    solver.main()