import time
import logging

class Part1():
    def __init__(self):
        self.almanac = {}
        self.seeds: list[int] = []
        self.mappings: dict[list[list[int], list[int]]] = {}
        self.categories = ["seeds", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
        logging.basicConfig(filename="logger.log", encoding="utf-8", level=logging.DEBUG, filemode="w")

    def read_data(self):
        with open("input.txt", "r") as f:
            data = f.read().split("\n\n")
        return data

    def populate_almanac(self, data):
        logging.info(f"Populating alamanc...")
        self.almanac["seeds"] = data[0].split(": ")[1].split(" ")
        self.almanac["soil"] = data[1].split("\n")[1:]
        self.almanac["fertilizer"] = data[2].split("\n")[1:]
        self.almanac["water"] = data[3].split("\n")[1:]
        self.almanac["light"] = data[4].split("\n")[1:]
        self.almanac["temperature"] = data[5].split("\n")[1:]
        self.almanac["humidity"] = data[6].split("\n")[1:]
        self.almanac["location"] = data[7].split("\n")[1:]
        logging.info("Almanac populated")
    
    def check_if_within_range(self, src: int, dest: int, length: int, current: int):
        src, dest, length, current = int(src), int(dest), int(length), int(current)
        if src <= current < (src + length):
            return dest + (current - src)
        else:
            return False

    def calculate_location(self, seed: int, key: str):
        flag = False
        value = self.almanac[key]
        response = 0
        for entry in value:
            dest, src, length = entry.split()
            response = self.check_if_within_range(src, dest, length, seed)
            if response is not False:                
                flag = True
                break
        
        if not flag:
            logging.error(f"Seed not mapped, returning original value")
            response = seed
            logging.info(f"New response value: {response}")
        
        if key == "location":
            return response
        else:
            next_category = self.categories[self.categories.index(key) + 1]
            logging.debug(f"Current category: {key}; Category index: {self.categories.index(key)}")
            logging.debug(f"Next category: {next_category}; Category index: {self.categories.index(key) + 1}")
            return self.calculate_location(response, next_category)
    
    def parse_seed_data(self):
        seed_bank = self.almanac["seeds"]
        for i in range(0, len(seed_bank), 2):
            seed_id, length = int(seed_bank[i]), int(seed_bank[i+1])
            for d in range(length):
                self.seeds.append(seed_id + d)

    def main(self):
        data = self.read_data()
        self.populate_almanac(data)
        print(self.almanac["seeds"])
        self.parse_seed_data()

        smallest = -1
        for seed in self.seeds:
            result = self.calculate_location(seed, "soil")
            if smallest == -1 or result < smallest:
                smallest = result

        logging.info("Execution complete")
        logging.info(f"Smallest location ID: {smallest}")


if __name__ == "__main__":

    part1 = Part1()
    start = time.time()
    part1.main()
    end = time.time()
    delta = end - start
    print(f"Total execution time: {delta} seconds")