class Part1():
    def __init__(self):
        self.schematic: list[str] = []
        self.symbol_locations: list[str] = []
        self.engine_component_id: list[int] = []
        self.digit_locations: list[str] = []

    def read_data(self):
        with open("sample.txt", "r") as f:
            document = f.read()
        return document

    def locate_symbols(self, segment_id: int, segment: str):
        for i in range(len(segment)):
            element = segment[i]
            if not element.isalnum() and element != ".":
                self.symbol_locations.append(f"{i}:{segment_id}")

    
    def check_adjacent_positions(self, coordinates: str):
        original_x, original_y = coordinates.split(":")
        original_x, original_y = int(original_x), int(original_y)
        print(f"Original location: {original_x}, {original_y}")
        for add_x in range(-1, 2):
            for add_y in range(-1, 2):
                x, y = original_x + add_x, original_y + add_y
                character = self.schematic[y][x]
                print(f"Current location: {x}, {y}. Current character: {character}")
                if character.isdigit():
                    print(f"Digit character found at location ({x}, {y}): {character}")
                    self.digit_locations.append(f"{x}, {y}")
        

    def main(self):
        self.schematic = self.read_data().split()
        print(self.schematic)
        for i in range(len(self.schematic)):
            self.locate_symbols(i, self.schematic[i])

        for coordinates in self.symbol_locations:
            self.check_adjacent_positions(coordinates)
        print(self.digit_locations)

if __name__ == "__main__":
    part1 = Part1()
    part1.main()