class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __repr__(self) -> str:
        return f"[{self.lower}, {self.upper}]"
    
    def intersection(self, other):
        """
        Returns the highest minimum and smallest maximum intersection points of 2 ranges as a Range() object, or None if the ranges do not intersect

        Example:
        ----------
                -------
        Code returns Range(8, 10)

        ---------
                    -----
        Code returns None
        """
        tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
        return tmp if tmp.lower < tmp.upper else None

    def subtraction(self, other) -> list:
        """
        Returns the subtraction of 2 intersecting ranges
        """
        intersection = self.intersection(other)
        if intersection == None:
            """
            If there are no intersections found, return Range() object containing the current lower and upper values

            Visualisation:
            --------          (Our range)
                     -------- (Intersecting range)
            """
            return [Range(self.lower, self.upper)]
        elif (intersection.lower, intersection.upper) == (self.lower, self.upper):
            """
            If the lower and upper values of the intersecting range is the same as ours, return an empty list

            Visualisation:
            -------- (Our range)
            -------- (Intersecting range)
            """
            return []
        elif intersection.lower == self.lower:
            """
            If the lower value of the intersecting range is the same as ours, return a Range() object with the upper values of the two ranges

            Visualisation:
            --------- (Our range)
            ---       (Intersecting range)
            """
            return [Range(intersection.upper, self.upper)]
        elif intersection.upper == self.upper:
            """
            If the upper value of the intersecting range is the same as ours, return a Range() object with the lower values of the two ranges

            Visualisation:
            ------- (Our range)
               ---- (Intersecting range)
            """
            return [Range(self.lower, intersection.lower)]
        else:
            """
            If none of the ranges' values match, return a list of two Range() objects containing the lower and upper values respectively

            Visualisation:
            --------- (Our range)
              ---     (Intersecting range)
            """
            return [Range(self.lower, intersection.lower), Range(intersection.upper, self.upper)]
    
    def add(self, offset: int | float):
        return Range(self.lower + offset, self.upper + offset)

class Map:
    def __init__(self, map_str):
        self.rules = []
        for line in map_str.splitlines()[1:]:
            # line = "50 98 2"
            # line.split() = ["50", "98", "2"]
            dest, src, size = map(int, line.split())
            self.rules.append((dest, src, size))
    
    def convert(self, _input):
        for dest, src, size in self.rules:
            if src <= _input < (src + size):
                return dest + _input - src
            
        return _input

class Part2():
    def __init__(self):
        self.maps = None
        self.answer = float('inf')

    def read_data(self):
        with open("sample.txt", "r") as f:
            return f.read().split("\n\n")
        
    def propagate(self, r: Range, layer: int):
        """
        Goes through each layer ("map") and process them until it reaches the final layer ("locations")
        """
        if layer == len(self.maps):
            self.answer = min(self.answer, r.lower)
            return
        
        for dest, src, size in self.maps[layer].rules:
            map_range = Range(src, src + size)
            intersection = r.intersection(map_range)
            if intersection is not None:
                self.propagate(intersection.add(dest - src), layer + 1)
                subtraction = r.subtraction(map_range)
                if len(subtraction) == 0:
                    # All the rules have been handled
                    return
                r = subtraction[0]
                if len(subtraction) == 2:
                    self.propagate(subtraction[1], layer)
        self.propagate(r, layer + 1)

    def get_location(self, seed, maps):
        for _map in maps:
            seed = _map.convert(seed)
        return seed

    def main(self):
        seeds, *map_strs = self.read_data()
        seeds = list(map(int, seeds.split()[1:]))
        self.maps = [Map(map_str) for map_str in map_strs]

        for i in range(0, len(seeds), 2):
            self.propagate(Range(seeds[i], seeds[i] + seeds[i + 1]), 0)
        print(self.answer)
        return None

if __name__ == "__main__":
    part2 = Part2()
    part2.main()