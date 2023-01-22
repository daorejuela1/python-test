#!/usr/bin/env python3
"""
Test for task_2.py
"""

import unittest
import os
import csv
import random
import string
from task_2 import DataGenerator

class TestStringMethods(unittest.TestCase):
    def test_file_existence(self):
        """
        Test if file exists
        """
        file_name = "test_data.csv"
        DataGenerator(100, file_name).write_data_to_csv_file()
        self.assertTrue(os.path.exists(file_name))
        os.remove(file_name)

    def test_file_content(self):
        """
        Test if file contains correct data
        """
        file_name = "test_data.csv"
        DataGenerator(100, file_name).write_data_to_csv_file()
        with open(file_name, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                self.assertTrue(row[0].isdigit())
                self.assertTrue(len(row[1]) == 10)
        os.remove(file_name)

    def test_file_quantity(self):
        """
        Test if file contains correct quantity of rows
        """
        file_name = "test_data.csv"
        DataGenerator(100, file_name).write_data_to_csv_file()
        with open(file_name, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            self.assertEqual(len(list(reader)), 100)
        os.remove(file_name)

    def test_file_content_random(self):
        """
        Test if file contains correct data
        """
        file_name = "test_data.csv"
        DataGenerator(100, file_name).write_data_to_csv_file()
        with open(file_name, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                self.assertTrue(int(row[0]) in range(1, 10000))
                self.assertTrue(len(row[1]) == 10)
                self.assertTrue(all(c in string.ascii_uppercase + string.digits for c in row[1]))
        os.remove(file_name)

if __name__ == "__main__":
    unittest.main()