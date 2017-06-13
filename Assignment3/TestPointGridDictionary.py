import unittest
from PointAndGrid import Point, Grid
from DictionaryClass import Dictionary

class TestPointAndGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid([['l', 'i', 'n', 'e'],
                          ['i', 'h', 's', 'g'],
                          ['n', 'd', 'i', 'o']])
        self.dictionary = Dictionary(['line', 'like', 'ego', 'dig'])

    ############################# TEST POINT CLASS.#################################################

    def testPointsOnEquality(self):
        p1 = Point(self.grid, (1, 1), 'h')
        p2 = Point(self.grid, (1, 1), 'h')
        self.assertEqual(p1, p2)

    def testPointCreationByInvalidValue(self):
        self.assertRaises(AttributeError, lambda: Point(self.grid, (1, 1), 'invalid element'))

    ############################## TEST GRID CLASS ##################################################

    def testGrid_SizeMethods(self):
        self.assertEqual(4, self.grid.horysontalSize())
        self.assertEqual(3, self.grid.verticalSize())

    def testGrid_AddValidRow(self):
        self.grid.addRow(['n', 'e', 'w', 'r'])

        expectedGrid = Grid([['l', 'i', 'n', 'e'],
                             ['i', 'h', 's', 'g'],
                             ['n', 'd', 'i', 'o'],
                             ['n', 'e', 'w', 'r']])

        self.assertEqual(self.grid, expectedGrid)


    def testGrid_AddInvalidRow(self):

        self.assertRaises(ValueError, lambda: self.grid.addRow(['n', 'e']))


    def testGrid_AddValidColumn(self):
        self.grid.addColumn(['c', 'o', 'l'])

        expectedGrid = Grid([['l', 'i', 'n', 'e', 'c'],
                             ['i', 'h', 's', 'g', 'o'],
                             ['n', 'd', 'i', 'o', 'l']])
        self.assertEqual(self.grid, expectedGrid)


    def testGrid_FindStringAndItsPresence(self):

        isPresent = self.grid.ifWordInGrid('line')
        actual = self.grid.findString('line')

        expected = [Point(self.grid, (0,0), 'l'),
                    Point(self.grid, (0,1), 'i'),
                    Point(self.grid, (0,2), 'n'),
                    Point(self.grid, (0,3), 'e')]

        self.assertEqual(actual, expected)
        self.assertTrue(isPresent)


    def testGrid_FindStringAndItsPresenceIfNotExists(self):

        isPresent = self.grid.ifWordInGrid('linese')
        notExists = self.grid.findString('linese')

        self.assertIsNone(notExists)
        self.assertFalse(isPresent)

    ############################## TEST DICTIONARY CLASS ##############################################

    def testDictionary_ListOfPrefixes(self):

        actual = self.dictionary.listOfPrefixes()
        expected = ['d', 'di', 'dig', 'e', 'eg', 'ego', 'l', 'li', 'lik', 'like', 'lin', 'line']
        self.assertEqual(actual, expected)


    def testDictionary_WordsInDictionary(self):

        actualList = self.dictionary.wordsInGrid(self.grid)
        expectedList = ['dig', 'ego', 'line']
        self.assertEqual(actualList, expectedList)


if __name__ == '__main__':
    unittest.main()