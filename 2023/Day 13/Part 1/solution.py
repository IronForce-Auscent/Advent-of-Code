import numpy as np

class Solver:
    def read_data(self):
        with open("sample.txt") as d:
            data = d.read()
        return data

    def get_rows_columns(self, data):
        columns = []
        rows = data
        for i in range(len(rows[0])):
            column = []
            for row in rows:
                column.append(row[i])
            columns.append("".join(column))
        return rows, columns

    def calculate_lines_of_reflection(self, data: list[str]):
        mirror_locations = []
        for entry in data:
            locations = []
            max_length = len(entry)
            for mirror in range(1, max_length, 1):
                if mirror in (1, 8):
                    continue
                left, right = entry[:mirror], entry[mirror:]
                print(f"Left half: {left}; Right half: {right}")
                if left[::-1] in right or right[::-1] in left:
                    locations.append(mirror)
            mirror_locations.append(locations)
        return mirror_locations

    def main(self):
        _, *datasets = self.read_data().split("\n\n")
        datasets = list(map(str.split, datasets))
        for dataset in datasets:
            rows, columns = self.get_rows_columns(dataset)
            mirror_locations = self.calculate_lines_of_reflection(rows)
            print(f"Mirror locations: {mirror_locations}")

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    solver = Solver()
    solver.main()
    mirror = time.perf_counter() - start
    print(f"Execution time: {mirror} seconds")