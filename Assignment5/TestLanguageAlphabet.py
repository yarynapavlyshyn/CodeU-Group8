from LanguageClass import Language
import unittest


class TestLanguage(unittest.TestCase):

    def setUp(self):
        self.language_same_length = Language(['ART', 'RAT', 'CAT', 'CAR'])
        self.language = Language(['ARTIST', 'RAT', 'CAT', 'CARROT', 'S'])
        self.language_alphabet = Language(['D', 'A', 'K', 'B', 'F'])
        self.language_empty = Language([])

    def testGetAlphabetSameLengthWords(self):
        actual = self.language_same_length.alphabet()
        expected = ['A', 'T', 'R', 'C']
        self.assertListEqual(actual, expected)

    def testGetAlphabetDifferentLengthWords(self):
        actual = self.language.alphabet()
        # may be multiple variants so we cam improve but it doesn't matter much :)
        expected = ['A', 'T', 'R', 'I', 'S', 'C', 'O']
        self.assertListEqual(actual, expected)

    def testGetAlphabetWordListIsAlphabet(self):
        actual = self.language_alphabet.alphabet()
        expected = ['D', 'A', 'K', 'B', 'F']
        self.assertListEqual(actual, expected)

    def testGetAlphabetEmptyLanguage_EmptyAlphabet(self):
        actual = self.language_empty.alphabet()
        expected = []
        self.assertListEqual(actual, expected)
