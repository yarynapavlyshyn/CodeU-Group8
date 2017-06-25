import unittest
from PointAndGrid import Point, Grid
from DictionaryClass import Dictionary

class TestPointAndGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid([['l', 'i', 'n', 'e'],
                          ['i', 'h', 's', 'g'],
                          ['n', 'd', 'i', 'o']])
        self.dictionary = Dictionary({'line', 'like', 'ego', 'dig'})
        # self.dictionary = Dictionary(['line', 'like', 'ego', 'dig']) # gives the same result

    ############################# TEST POINT CLASS #################################################

    def testPointsOnEquality(self):
        p1 = Point(self.grid, (1, 1), 'h')
        p2 = Point(self.grid, (1, 1), 'h')
        p3 = Point(self.grid, (1, 2), 's')

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def testPointCreationByInvalidValue(self):

        self.assertRaises(ValueError, lambda: Point(self.grid, (1, 1), 'invalid element'))

    ############################## TEST GRID CLASS ##################################################

    def testGrid_SizeMethods(self):

        self.assertEqual(4, self.grid.horizontalSize())
        self.assertEqual(3, self.grid.verticalSize())

    def testGrid_FindStringAndItsPresence(self):

        actual = self.grid.findString('line') # find path
        expected = [Point(self.grid, (0,0), 'l'),
                    Point(self.grid, (0,1), 'i'),
                    Point(self.grid, (0,2), 'n'),
                    Point(self.grid, (0,3), 'e')]

        self.assertEqual(actual, expected)
        self.assertTrue(self.grid.findString('line'))

    def testGrid_FindStringAndItsPresenceIfNotExist(self):

        self.assertIsNone(self.grid.findString('linearity'))
        self.assertIsNone(self.grid.findString('z'))
        self.assertFalse(self.grid.ifWordInGrid('linearity'))

    ############################## TEST DICTIONARY CLASS ##############################################

    def testDictionary_Words(self):

        actual = self.dictionary.words()
        expected = {'dig', 'ego', 'like', 'line'}

        self.assertEqual(actual, expected)

    def testDictionary_IfIsWord(self):

        self.assertFalse(self.dictionary.isWord('pink'))
        self.assertTrue(self.dictionary.isWord('dig'))
        self.assertFalse(self.dictionary.isWord('di'))
        self.assertTrue(self.dictionary.isWord('like'))


    def testDictionary_ListOfPrefixes(self):

        actual = self.dictionary.prefixes()
        expected = {'d', 'di', 'dig', 'e', 'eg', 'ego', 'l', 'li', 'lik', 'like', 'lin', 'line'}

        self.assertEqual(actual, expected)

    def testDictionary_IfIsPrefix(self):

        self.assertTrue(self.dictionary.isPrefix('l'))
        self.assertTrue(self.dictionary.isPrefix('dig'))
        self.assertFalse(self.dictionary.isPrefix('s'))

    def testDictionary_WordsInGrid(self):

        actual = self.dictionary.wordsInGrid(self.grid)
        expected = {'dig', 'ego', 'line'}

        self.assertSetEqual(actual, expected)

    def testDictionary_DeleteWordIfExists(self):

        self.dictionary.deleteWord('like')
        actual = self.dictionary.words()
        expected = {'dig', 'line', 'ego'}
        actualPref = self.dictionary.prefixes()
        expectedPref = {'di', 'line', 'e', 'eg', 'd', 'li', 'ego', 'l', 'dig', 'lin'}

        self.assertSetEqual(actual, expected)
        self.assertSetEqual(actualPref, expectedPref)

    def testDictionary_DeleteWordIfNotExist(self):

        self.assertRaises(ValueError, lambda: self.dictionary.deleteWord('lie'))

if __name__ == '__main__':
    unittest.main()
