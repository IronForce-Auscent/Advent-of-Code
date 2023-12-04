class Part1():
    def __init__(self):
        self.schematic = None
        self.valid_numbers = []
        self.non_symbols = "0123456789."
        self.max_x = 0 # length 10 for modified_sample
        self.max_y = 0 # length 13 for modified_sample

    def read_data(self):
        with open("testcases.txt", "r") as f:
            self.schematic = f.read()
    
    def get_neighbour_coordinates(self, x: int, y: int) -> list[list[int, int]]:
        coordinates = []
        for dtx in (-1, 0, 1):
            for dty in (-1, 0, 1):
                if (dtx, dty) == (0, 0):
                    continue                
                new_x, new_y = x, y
                if 0 <= (x + dtx) < self.max_x:
                    new_x = x + dtx
                else:
                    new_x = x
                if 0 <= (y + dty) < self.max_y:
                    new_y = y + dty
                else:
                    new_y = y
                coordinates.append([new_x, new_y])
        return coordinates
    
    def check_neighbours(self, x: int, y: int):
        neighbours = self.get_neighbour_coordinates(x, y)
        for neighbour in neighbours:
            nbx, nby = neighbour[0], neighbour[1]
            if self.schematic[nby][nbx] not in self.non_symbols:
                return True
            else:
                continue
        return False
        
    def calculate_valid_engine_parts(self):
        x, y = 0, 0
        while y < self.max_y:
            x = 0
            while x < self.max_x:
                current_char = self.schematic[y][x]
                if current_char.isdigit():
                    number = ""
                    peek_x = x
                    while current_char.isdigit():
                        number += current_char
                        if peek_x + 1 < self.max_x:
                            peek_x += 1
                            current_char = self.schematic[y][peek_x]
                        else:
                            current_char = "."
                    print(f"Peek value :{peek_x}")
                    print(number)
                    for num_x in range(x, peek_x):
                        print(num_x)
                        response = self.check_neighbours(num_x, y)
                        if response:
                            self.valid_numbers.append(int(number))
                            break
                    x = peek_x
                x += 1
            y += 1

    def generate_guardroom(self):
        x = "."*self.max_x
        y = []
        y.append(x)
        for line in self.schematic:
            tmp = "." + line + "."
            y.append(tmp)
        y.append(x)
        self.schematic = y
    
    def update_border_lengths(self):
        self.max_x = len(self.schematic[0])
        self.max_y = len(self.schematic)


    def main(self):
        self.read_data()
        self.schematic = self.schematic.split()
        self.update_border_lengths()
        self.generate_guardroom()
        self.update_border_lengths()
        self.calculate_valid_engine_parts()
        print(self.valid_numbers)
        print(sum(self.valid_numbers))

if __name__ == "__main__":
    part1 = Part1()
    part1.main()