from dotenv import load_dotenv
from utils.aoc_input import AOC_Input
from typing import *

import importlib
import argparse
import time
import os

YEAR = 2023
SESS_KEY = os.getenv("AOC_SESSION")

load_dotenv()

parser = argparse.ArgumentParser(description="Select a day to run and submit solution for")
parser.add_argument("--day", dest="day", action="store", required=True, help="The day to test solutions for")
parser.add_argument("--submit", dest="submit", action="store_true", default="False", help="Submit the solution(s) generated to AoC's website")

class ConsolidatedTester:

    def __init__(self, day: int):
        self.day = day

        AoC_Input = AOC_Input(year=YEAR, _clear_data_folder=False)
        AoC_Input.get_data()    

    def get_module_by_day(self):
        return importlib.import_module(f"src.day_{self.day}")

    def get_input_data_by_day(self):
        input_loc = f"data/{YEAR}_{self.day}.txt"
        with open(input_loc, "r") as f:
            data = f.read()
        return data
    
    def main(self):
        module = self.get_module_by_day()
        data = self.get_input_data_by_day()
        solver = module.Solver(data)
        start = time.perf_counter()
        try:
            results = solver.main()
        except Exception as e:
            results = ("Exception: {e}", None)
        end = time.perf_counter()
        runtime = end - start
        return results, runtime

if __name__ == "__main__":
    args = parser.parse_args()
    tester = ConsolidatedTester(day=args.day)
    results, runtime = tester.main()
    print(f"Part 1: {results[0]}")
    print(f"Part 2: {results[1]}")
    print(f"Runtime: {runtime}")