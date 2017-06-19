from PointAndGrid import Point, Grid

class Dictionary:

    def __init__(self, sequenceOfWords = None):
        """
        For Dictionary initialization with optional set of words.
        :param setOfWords: any iterable sequence
        :return: None
        """
        if sequenceOfWords is None:
            self._words = set()
        else:
            self._words = set([w.lower() for w in sequenceOfWords])
        self._prefixes = dict()
        self._updatePrefixes()

    def words(self):
        """
        Return a set of words in dictionary.
        :return: set(str)
        """
        return self._words

    def addWord(self, word):
        """
        Add the word to the dictionary.
        :param word: str
        :return: None
        """
        word = word.lower()
        if word in self._words:
            raise ValueError("there already exists such a word")
        self._words.add(word)
        self._updatePrefixes(word)

    def deleteWord(self, word):
        """
        Delete a word from dictionary and its prefixes from the self._prefixes if they are not prefixes of other words.
        Raise ValueError if word is not in dictionary.
        :param word: string
        :return: None or raises ValueError
        """
        word = word.lower()
        if word not in self._words:
            raise ValueError("there is not such a word")

        self._words.remove(word)
        prefs = self._wordPrefixes(word)
        for pref in prefs:
            if self._prefixes[pref] == 1:
                self._prefixes.pop(pref)
            else:
                self._prefixes[pref] -= 1

    def size(self):
        """
        Return the size of dictionary - length of the list of words.
        :return: int
        """
        return len(self._words)

    def isWord(self, word):
        """
        Check if there exists such a word in the dictionary.
        :param word: str
        :return: bool
        """
        return word.lower() in self._words

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
        return set(self._prefixes)

    def wordsInGrid(self, grid):
        """
        Returns all words in the dictionary thet can be formed in the grid.
        :return: set(str)
        """
        result = set()
        for word in self._words:
            if grid.ifWordInGrid(word):
                result.add(word)
        return result if result else None

    def _updatePrefixes(self, word = None):
        """
        If argument word is given add all prefixes in word to self.prefixes, add all prefixes in all words in dictionary.
        :param word: string or None
        :return: set
        """
        if word:
            newPrefixes = self._wordPrefixes(word)
            for pref in newPrefixes:
                if pref in self._prefixes:
                    self._prefixes[pref] += 1
                else:
                    self._prefixes[pref] = 1
        else:
            for w in self._words:
                self._updatePrefixes(w)

    def _wordPrefixes(self, word):
        """
        Return a list of prefixes in the word.
        :param word: str
        :return: list(string)
        """
        return [ word[:i] for i in range(1, len(word) + 1) ]

    def __str__(self):
        """
        For string representation of Dictionary.
        :return: str
        """
        return str(self._words)

    def __len__(self):
        return self.size()
