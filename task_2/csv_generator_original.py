#!/usr/bin/env python3
"""
Generate csv file with random data
"""
import csv
import random
import string
import argparse
import time


class DataGenerator:
    """
    Class for generating random data and writing it to csv file
    """

    def __init__(self, quantity: int = 1000, file_name: str = "data.csv"):
        self.quantity = quantity
        self.file_name = file_name
        self.rows = []

    def generate_random_data(self):
        """
        Generate random data
        """
        for _ in range(self.quantity):
            self.rows.append(
                [
                    random.randint(1, 10000),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                ]
            )

    def write_data_to_csv_file(self):
        """
        Write data to csv file

        :param file_name: Name of the csv file
        """
        self.generate_random_data()
        with open(self.file_name, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            for row in self.rows:
                writer.writerow(row)
        print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("task_2.py")
    parser.add_argument("-o", "--output", help="output path to csv file", default="data.csv")
    parser.add_argument("-n", "--number-rows", help="number of rows to generate", default=1000, type=int)
    args = parser.parse_args()
    start_time = time.time()
    DataGenerator(args.number_rows, args.output).write_data_to_csv_file()
    print("--- %s seconds ---" % (time.time() - start_time))
