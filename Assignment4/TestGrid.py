import unittest
from PointGrid import Grid


class TestGridMethods(unittest.TestCase):

    def setUp(self):
        self.empty_grid = Grid([[]])
        self.small_grid = Grid([['T','T','F'],
                                ['T','F','T']])
        self.big_grid = Grid([['T', 'T', 'F', 'F', 'F', 'F', 'T'],
                              ['T', 'T', 'F', 'F', 'F', 'F', 'T'],
                              ['F', 'F', 'F', 'F', 'F', 'F', 'T'],
                              ['F', 'F', 'F', 'T', 'T', 'F', 'T'],
                              ['T', 'T', 'F', 'F', 'F', 'F', 'T'],
                              ['T', 'T', 'F', 'F', 'F', 'F', 'T'],
                              ['F', 'T', 'F', 'F', 'F', 'F', 'T']])
        self.the_sea = Grid([['F','F','F'],
                             ['F','F','F']])
        self.big_island = Grid([['T','T','T'],
                                ['T','T','T']])

    def test_get_element(self):
        expected = 'F'
        actual = self.big_grid.get_element((2, 2))
        self.assertEqual(actual, expected)

    def test_get_point(self):
        expected = Grid.Point('F', (2, 2))
        actual = self.big_grid.get_point((2, 2))
        self.assertEqual(actual, expected)

    def test_find_land(self):
        expected = [(0, 0), (0, 1), (1, 0), (1, 2)]
        actual = [p.coordinates for p in self.small_grid.find_land()]
        self.assertListEqual(actual, expected)

    def test_find_islands_small_grid(self):
        expected = [[(0, 0), (0, 1), (1, 0)], [(1, 2)]]
        actual = self.small_grid.find_islands()
        self.assertListEqual(actual, expected)

    def test_find_islands_empty_grid(self):
        actual = self.empty_grid.find_islands()
        self.assertIsNone(actual)

    def test_find_islands_big_grid(self):
        expected = [[(0, 0), (0, 1), (1, 1), (1, 0)],
                  [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)],
                  [(3, 3), (3, 4)],
                  [(4, 0), (4, 1), (5, 1), (5, 0), (6, 1)]]
        actual = self.big_grid.find_islands()
        self.assertListEqual(actual, expected)

    def test_all_land(self):
        expected = [[(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0)]]
        actual = self.big_island.find_islands()
        self.assertListEqual(actual, expected)

    def test_all_water(self):
        actual = self.the_sea.find_islands()
        self.assertIsNone(actual)

if __name__ == '__main__':
    unittest.main()
