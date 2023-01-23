#!/usr/bin/env python3
"""
Generate csv file with random data
"""
import csv
import random
import string
import argparse
import time
from concurrent.futures import ProcessPoolExecutor

POOL_WORKERS = 10


class DataGenerator:
    """
    Class for generating random data and writing it to csv file
    """

    def __init__(self, quantity: int = 1000, file_name: str = "data.csv"):
        """
        Set quantity of rows to generate and file name

        :param quantity: Quantity of rows to generate

        :param file_name: Name of the csv file
        """
        self.quantity = quantity
        self.file_name = file_name
        self._rows_to_generate = self.quantity // POOL_WORKERS

    def generate_random_data(self):
        """
        Generates random data according to the quantity of rows to generate
        """
        rows = []
        for _ in range(self._rows_to_generate):
            # Each row is a list of 1 number and 5 random strings
            rows.append(
                [
                    random.randint(1, 10000),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                ]
            )
        return rows

    def write_data_to_csv_file(self):
        """
        Writes data to csv file
        """
        with open(self.file_name, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            with ProcessPoolExecutor(max_workers=POOL_WORKERS) as executor:
                futures = [executor.submit(self.generate_random_data) for _ in range(POOL_WORKERS)]
            for future in futures:
                # Write rows inside each future to csv file
                writer.writerows(future.result())
        print(f"File {self.file_name} is ready with {self.quantity} rows")


if __name__ == "__main__":
    """
    Main function
    """
    parser = argparse.ArgumentParser("task_2.py")
    parser.add_argument("-o", "--output", help="output path to csv file", default="data.csv")
    parser.add_argument("-n", "--number-rows", help="number of rows to generate", default=1000, type=int)
    args = parser.parse_args()
    start_time = time.time()
    DataGenerator(args.number_rows, args.output).write_data_to_csv_file()
    print("--- %s seconds ---" % (time.time() - start_time))
