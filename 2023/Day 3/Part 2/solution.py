class Part2():
    def __init__(self):
        pass

    def read_data(self):
        with open("testcases.txt", "r") as f:
            document = f.read()
        return document

    def main(self):
        data = self.read_data()

if __name__ == "__main__":
    part2 = Part2()
    part2.main()