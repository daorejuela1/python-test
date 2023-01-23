#!/usr/bin/env python3
"""
Test for task_2.py
"""

import unittest
import os
import csv
import string
from csv_generator import DataGenerator
TEST_FILE_NAME = "test_data.csv"
TEST_ROWS_QUANTITY = 100


class TestStringMethods(unittest.TestCase):
    def test_file_existence(self):
        """
        Test if file exists
        """
        DataGenerator(TEST_ROWS_QUANTITY, TEST_FILE_NAME).write_data_to_csv_file()
        self.assertTrue(os.path.exists(TEST_FILE_NAME))
        os.remove(TEST_FILE_NAME)

    def test_file_content(self):
        """
        Test if file contains correct data
        """
        DataGenerator(TEST_ROWS_QUANTITY, TEST_FILE_NAME).write_data_to_csv_file()
        with open(TEST_FILE_NAME, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                self.assertTrue(row[0].isdigit())
                self.assertTrue(len(row[1]) == 10)
        os.remove(TEST_FILE_NAME)

    def test_file_quantity(self):
        """
        Test if file contains correct quantity of rows
        """
        DataGenerator(TEST_ROWS_QUANTITY, TEST_FILE_NAME).write_data_to_csv_file()
        with open(TEST_FILE_NAME, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            self.assertEqual(len(list(reader)), 100)
        os.remove(TEST_FILE_NAME)

    def test_file_content_random(self):
        """
        Test if file contains correct data
        """
        DataGenerator(TEST_ROWS_QUANTITY, TEST_FILE_NAME).write_data_to_csv_file()
        with open(TEST_FILE_NAME, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                self.assertTrue(int(row[0]) in range(1, 10000))
                self.assertTrue(len(row[1]) == 10)
                self.assertTrue(all(c in string.ascii_uppercase + string.digits for c in row[1]))
        os.remove(TEST_FILE_NAME)


if __name__ == "__main__":
    unittest.main()
