class Solver:
    def read_data(self):
        with open("sample.txt") as d:
            data = d.read()
        return data

    def main(self):
        data = self.read_data()


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    solver = Solver()
    solver.main()
    delta = time.perf_counter() - start
    print(f"Execution time: {delta} seconds")