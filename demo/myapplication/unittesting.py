# Name: bansri shah
# course: CST8333 Programming Language Research Project.
# Assignment 4
# student-number: 040920837
import unittest
import csv

print(" Student name: Bansri shah")
# CHECKING : Is the first record, with data values,read from the dataset what we expect .
# For that i create testcase for it
class app3(unittest.TestCase):
    # we create function to check test case
    def test(self):
        with open('13100262.csv', "r") as csv_files:
            csv_data = csv.reader(csv_files, delimiter=',')
            total = [lines for lines in csv_data]
# here function return true if first row from csv is same as we define below
        self.assertTrue(total[1],('2002', 'Canada', ' ', 'Males', '11 years', 'Rarely or never', 'Percent', 239, 'units ', 0, 'v30413271', '1.1.1.1', 31, '', '', '', 0))




if __name__ == '__main__':
            unittest.main()