from aocd import get_data

import aocd.exceptions

import time
import os.path
import os
import glob
import logging

class AOC_Input:

    def __init__(self, year: int, _get_all: bool = False, _clear_data_folder: bool = False):
        self.days: list[int] = [_ for _ in range(1, 26)]
        self.year: int = year
        self._get_all: bool = _get_all
        self._clear_data_folder: bool = _clear_data_folder
        self._logger: logging.Logger = logging.getLogger()
        print(self._logger)

        if self._clear_data_folder:
            self.clear_data()

    def get_data(self):
        for day in self.days:
            input_loc = f"data/{self.year}_{day}.txt"
            if os.path.isfile(input_loc):
                logging.info(f"Input data for {self.year} day {day} exists, skipping...")
                continue
            try:
                data = get_data(day=day, year=self.year)
                with open(input_loc, "w") as f:
                    f.write(data)
                    logging.info(f"Input data for {self.year} day {day} retrieved and saved")
            except aocd.exceptions.PuzzleLockedError as PuzzleLocked:
                logging.info(f"All available inputs retrieved, exiting...")
                return
            time.sleep(0.5) # To avoid getting rate limited
        logging.info(f"All 25 days retrieved")
    
    def clear_data(self):
        files = glob.glob("/data/*")
        for f in files:
            os.remove(f)
        logging.info(f"All input data files cleared")
