from PointAndGrid import Point, Grid

class Dictionary:

    def __init__(self, setOfWords = {}):
        """
        For Dictionary initialization with optional list of words.
        :param listOfWords: set(str) or None
        :return: None
        """
        self.words = set(listOfWords) # to avoid dublicates
        self._prefixes = set()
        self._updatePrefixes()

    def addWord(self, word):
        """
        Add the word to the dictionary.
        :param word: str
        :return: None
        """
        self.words.add(word)
        self._updatePrefixes(word)

    def size(self):
        """
        Return the size of dictionary - length of the list of words.
        :return: int
        """
        return len(self.words)

    def isWord(self, word):
        """
        Check if there exists such a word in the dictionary.
        :param word: str
        :return: bool
        """
        return word in self.words

    def isPrefix(self, word):
        """
        Return True if the wod is one of the prefixes of the dictionary, false otherwise.
        :param word: str
        :return: bool
        """
        return word in self._prefixes

    def prefixes(self):
        """
        Return the list of all prefixes in the dictionary.
        :return: set(string)
        """
        return self._prefixes

    def wordsInGrid(self, grid):
        """
        Returns all words in the dictionary thet can be formed in the grid.
        :return: set(str)
        """
        result = set()
        for word in self.words:
            if grid.ifWordInGrid(word):
                result.add(word)
        return result

    def _updatePrefixes(self, word = None):
        """
        If argument word is given add all prefixes in word to self.prefixes, add all prefixes in all words in dictionary.
        :param word: string or None
        :return: set
        """
        if word:
            self._prefixes = self._prefixes.union(self._wordPrefixes(word))
            return
        for w in self.words:
            self._updatePrefixes(w)

    def _wordPrefixes(self, word):
        """
        Return a set of all prefixes in the word.
        :param word: str
        :return: set
        """
        return set([ word[:i] for i in range(1, len(word) + 1) ])
