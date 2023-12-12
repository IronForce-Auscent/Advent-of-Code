class Solver:
    def read_data(self):
        with open("input.txt") as d:
            data = d.read().splitlines()
        return data

    def generate_variations(self, base: str):
        variations = []

        def generate_helper(current_str: str, index: int):
            if index == len(current_str):
                variations.append(current_str)
                return
            
            if current_str[index] == "?":
                generate_helper(current_str[:index] + "." + current_str[index + 1:], index + 1)
                generate_helper(current_str[:index] + "#" + current_str[index + 1:], index + 1)
            else:
                generate_helper(current_str, index + 1)
        
        generate_helper(base, 0)
        return variations
    
    def check_variations(self, variations: list[str], config: list[str]):
        valid_variations = []
        for variation in variations:
            malfunctions = [x for x in variation.split(".") if x != ""]
            if len(malfunctions) != len(config):
                continue
            checks = []
            for malfunction, config_value in zip(malfunctions, config):
                if len(malfunction) == int(config_value):
                    checks.append(True)
                else:
                    pass
            if len(checks) == len(config):
                valid_variations.append(variation)

        return list(dict.fromkeys(valid_variations))

    def main(self):
        data = self.read_data()
        rows, configs = [], []
        for entry in data:
            row, config = entry.split()
            rows.append(row)
            configs.append(config.split(","))
        
        sum_variations = []
        for row, config in zip(rows, configs):
            print(f"Row: {row}; Configuration: {config}")
            variations = self.generate_variations(row)
            valid_variations = self.check_variations(variations, config)
            sum_variations.append(len(valid_variations))
        
        print(f"Valid variations: {sum_variations}")
        print(f"Answer: {sum(sum_variations)}")


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    solver = Solver()
    solver.main()
    delta = time.perf_counter() - start
    print(f"Execution time: {delta} seconds")