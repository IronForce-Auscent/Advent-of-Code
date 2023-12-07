class Part1():
    def __init__(self):
        self.duration = 0
        self.record = 0

    def read_data(self):
        with open("input.txt", "r") as f:
            document = f.read()
        return document
    
    def evaluate(self, race_time: int, record: int):
        count = 0
        for charge_time in range(race_time):
            dist = charge_time * race_time - charge_time ** 2
            if dist > record:
                count += 1
        return count
    
    def parse_data(self, data: list):
        d, r = list(map(str.split, data))
        d, r = d[1:], r[1:]
        d, r = list(map(''.join, (d, r)))
        return list(map(int, (d, r)))


    def main(self):
        data = self.read_data().split("\n")
        self.duration, self.record = self.parse_data(data)
        total = 1
        res = self.evaluate(self.duration, self.record)
        total *= res
        print(total)

if __name__ == "__main__":
    part1 = Part1()
    part1.main()