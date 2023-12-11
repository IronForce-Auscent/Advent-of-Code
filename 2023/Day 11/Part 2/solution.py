import numpy as np
import tcod
import itertools

class Solver():
    def __init__(self):
        self.universe = None
        self.empty_columns = None
        self.empty_rows = None
        self.coordinates = []

    def read_data(self):
        with open("input.txt", "r") as f:
            document = f.read().splitlines()
        return document
    
    def parse_to_2d_array(self, universe: list[str]):
        parsed = []
        for section in universe:
            parsed.append([x for x in section])
        array = np.array(parsed)
        return array
    
    def count_empty_sections(self):
        rows, columns = self.universe.shape
        empty_rows, empty_columns = [], []
        for row in range(rows):
            if "#" not in self.universe[row, :]:
                empty_rows.append(row)
        
        for column in range(columns):
            if "#" not in self.universe[:, column]:
                empty_columns.append(column)
        
        return empty_rows, empty_columns
    
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
    
    def expand_coordinates(self, coordinates: tuple[int, int], multiplier: int):
        empty_columns_before = sum([1 for col in self.empty_columns if col < coordinates[1]])
        empty_rows_before = sum([1 for row in self.empty_rows if row < coordinates[0]])
        return (coordinates[1] + empty_columns_before * (multiplier - 1), 
                coordinates[0] + empty_rows_before * (multiplier - 1))
                

    def main(self):
        universe = self.read_data()
        self.universe = self.parse_to_2d_array(universe)
        self.empty_rows, self.empty_columns = self.count_empty_sections()
        print(self.empty_rows, self.empty_columns)
        self.coordinates = self.parse_galaxies()
        
        expanded_coordinates = []
        for coordinates in self.coordinates:
            x, y = reversed(coordinates)
            new_x, new_y = self.expand_coordinates((x, y), 1_000_000)
            expanded_coordinates.append((new_x, new_y))
        

        pairings = list(itertools.combinations(expanded_coordinates, 2))
        distances = []
        for pairing in pairings:
            start, end = pairing
            distance = self.calculate_manhatten_distance(start, end)
            distances.append(distance)

        print(f"Sum of distances: {sum(distances)}")

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    solver = Solver()
    solver.main()
    delta = time.perf_counter() - start
    print(f"Execution time: {delta} seconds")