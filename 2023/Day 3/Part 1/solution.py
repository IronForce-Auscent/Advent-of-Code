class Solver():
    def __init__(self):
        self.number_locations = {}
        self.valid_ids = []
        self.schematics = []
        self.valid_chars = "0123456789."

    def read_data(self):
        with open("modified.txt", "r") as f:
            document = f.read().splitlines()
        return document
    
    def get_numloc(self, schematics: list[str]):
        for y, schematic in enumerate(schematics):
            i = 0
            while i < len(schematic):
                current_char = schematic[i]
                if current_char.isdigit():
                    new_num = ""
                    for n in range(3):
                        current_char = schematic[i+n]
                        if not current_char.isdigit():
                            break
                        new_num += str(current_char)
                    if int(new_num) not in self.number_locations.keys():
                        self.number_locations[int(new_num)] = [(i + x, y) for x in range(0, len(new_num))]
                    else:
                        self.number_locations[int(new_num)].extend([(i + x, y) for x in range(0, len(new_num))])
                    i += len(new_num)
                i += 1

    def create_guardrails(self, schematics: list[str]):
        new_schematic = []
        x, y = len(schematics[0]), len(schematics)
        top_bottom_guardrails = ''.join("." for _ in range(x + 2))
        new_schematic.append(top_bottom_guardrails)
        for schematic in schematics:
            n = "." + schematic + "."
            new_schematic.append(n)
        new_schematic.append(top_bottom_guardrails)
        return new_schematic

    def check_neighbors(self):
        for number, coordinates in self.number_locations.items():
            print(f"Current number: {number}; Current coordinate set: {coordinates}")
            jump_to_next = False
            for coordinate in coordinates:
                if jump_to_next:
                    break
                for dtx in (-1, 0, 1):
                    if jump_to_next:
                        break
                    for dty in (-1, 0, 1):
                        if (dtx, dty) == (0, 0):
                            continue
                        new_x, new_y = coordinate[0] + dtx, coordinate[1] + dty
                        if (new_x, new_y) in coordinates:
                            continue

                        if str(self.schematics[new_y][new_x]) not in self.valid_chars:
                            print(f"Valid number: {number}")
                            self.valid_ids.append(number)
                            jump_to_next = True

    def main(self):
        schematic = self.read_data()
        padded_schematic = self.create_guardrails(schematic)
        """
        Padded schematic: 
        ['............', '.467..114...', '....*.......', '...35..633..', '.......#....', '.617*.......', '......+.58..', 
        '...592......', '.......755..', '....$.*.....', '..664.598...', '............']
        """
        self.get_numloc(padded_schematic)
        print(self.number_locations)
        self.schematics.extend(padded_schematic)
        self.check_neighbors()
        print(f"Valid IDs: {self.valid_ids}")
        print(f"Sum of IDs: {sum(self.valid_ids)}")


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    solver = Solver()
    solver.main()
    delta = time.perf_counter() - start
    print(f"Execution time: {delta} seconds")