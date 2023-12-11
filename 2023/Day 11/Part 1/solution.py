import numpy as np
import tcod
import itertools

class Solver():
    def __init__(self):
        self.universe = None
        self.coordinates = []

    def read_data(self):
        with open("sample.txt", "r") as f:
            document = f.read().splitlines()
        return document
    
    def parse_to_2d_array(self, universe: list[str]):
        parsed = []
        for section in universe:
            parsed.append([x for x in section])
        array = np.array(parsed)
        return array
    
    def expand_universe(self):
        # Calculate the number of rows and columns in the matrix
        rows, columns = self.universe.shape
        empty_rows, empty_columns = [], []
        for row in range(rows):
            if "#" not in self.universe[row, :]:
                empty_rows.append(row)
        
        for column in range(columns):
            if "#" not in self.universe[:, column]:
                empty_columns.append(column)
        
        padding_row = np.full((1, columns), ".") # Generate a padding row based on the current number of columns
        self.universe = np.insert(self.universe, tuple(empty_rows), padding_row, axis=0) # Add n number of padding rows to the matrix, at locations specified in empty_rows


        rows, _ = self.universe.shape # Recalculate the number of rows
        padding_column = np.full((rows, 1), ".") # Generate a padding column based on the new number of rows
        self.universe = np.insert(self.universe, tuple(empty_columns), padding_column, axis=1)

        rows, columns = self.universe.shape # Final recalculation of universe x and y limits
        # Regenerate the padding column and row
        padding_row = np.full((1, columns), ".")
        padding_column = np.full((rows, 1), ".")

        if rows > columns:
            for _ in range(rows - columns):
                self.universe = np.insert(self.universe, 0, padding_column, axis=1)
        else:
            for _ in range(columns - rows):
                self.universe = np.insert(self.universe, 0, padding_row, axis=0)

        return 0
    
    def parse_galaxies(self):
        max_x, max_y = reversed(self.universe.shape) # Calculate maximum values of x and y
        coordinates = []
        count = 1
        for y in range(max_y):
            for x in range(max_x):
                current_char = self.universe[y][x]
                if current_char == "#":
                    self.universe[y][x] = 0
                    coordinates.append((x, y))
                    #coordinates[count] = (x, y)
                    count += 1
                elif current_char == ".":
                    self.universe[y][x] = 1
        
        self.universe = self.universe.astype(int)
        return coordinates
    
    def calculate_manhatten_distance(self, origin: tuple[int, int], destination: tuple[int, int]):
        return abs(origin[0] - destination[0]) + abs(origin[1] - destination[1])

    def main(self):
        universe = self.read_data()
        self.universe = self.parse_to_2d_array(universe)
        self.expand_universe()
        coordinates = self.parse_galaxies()
        print(f"Coordinates of galaxies: {coordinates}")
        
        self.coordinates = coordinates
        pairings = list(itertools.combinations(self.coordinates, 2))
        distances = []
        for pairing in pairings:
            start, end = pairing
            distance = self.calculate_manhatten_distance(start, end)
            distances.append(distance)
        print(f"All distances: {distances}")
        print(f"Sum of distances: {sum(distances)}")


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    solver = Solver()
    solver.main()
    delta = time.perf_counter() - start
    print(f"Execution time: {delta} seconds")