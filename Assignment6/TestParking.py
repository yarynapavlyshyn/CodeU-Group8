import unittest
from RearrangingCars import Parking

class TestRearrangingParking(unittest.TestCase):
    def setUp(self):
        self.parking = Parking([1, 2, 0, 3])
        self.destination1 = [3, 1, 0, 2]
        self.destination2 = [0, 2, 3, 1]
        self.destination3 = [3, 1, 2, 0]
        self.empty_parking = Parking([])
        self.destination_is_parking = [1, 2, 0, 3]

    def testing_different_destinations(self):
        expected1 = [[1, 2, 0, 3],
                     [0, 2, 1, 3],
                     [3, 2, 1, 0],
                     [3, 0, 1, 2],
                     [3, 1, 0, 2]]
        actual1 = self.parking.rearrange(self.destination1)
        self.assertListEqual(actual1, expected1)

        expected2 = [[1, 2, 0, 3],
                     [1, 2, 3, 0],
                     [0, 2, 3, 1]]
        actual2 = self.parking.rearrange(self.destination2)
        self.assertListEqual(actual2, expected2)

        expected3 = [[1, 2, 0, 3],
                     [1, 0, 2, 3],
                     [0, 1, 2, 3],
                     [3, 1, 2, 0]]
        actual3 = self.parking.rearrange(self.destination3)
        self.assertListEqual(actual3, expected3)

    def test_empty_parking(self):
        expected = []
        actual = self.empty_parking.rearrange([])
        self.assertListEqual(actual, expected)

    def test_destination_is_parking(self):
        expected = []
        actual = self.parking.rearrange(self.destination_is_parking)
        self.assertListEqual(actual, expected)
