class Solver():
    def __init__(self):
        pass

    def read_data(self):
        with open("sample.txt", "r") as f:
            document = f.read()
        return document

    def main(self):
        data = self.read_data()

if __name__ == "__main__":
    solver = Solver()
    solver.main()