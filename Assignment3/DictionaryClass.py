from PointAndGrid import Point, Grid

class Dictionary:
    def __init__(self, listOfWords = []):
        """
        For Dictionary initialization with optional list of words.
        :param listOfWords: list
        :return: None
        """
        self.words = listOfWords

    def addWord(self, word):
        """
        Add the word to the dictionary.
        :param word: str
        :return: None
        """
        self.words.append(word)

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
        if word in self.words:
            return True
        return False

    def isPrefix(self, word):
        """
        Return True if the wod is one of the prefixes of the dictionary, false otherwise.
        :param word:
        :return: bool
        """
        if word in self.listOfPrefixes():
            return True
        return False

    def listOfPrefixes(self):
        """
        Return the list of all prefixes in the dictionary.
        :return: list(string)
        """
        prefixes = []
        for word in self.words:
            for i in range(len(word)):
                pref = word[:i]
                if pref not in prefixes:
                    prefixes.append(pref)
        return prefixes


    def wordsInGrid(self, grid):
        """
        Returns all words in the dictionary thet can be formed in the grid.
        :return: list(str)
        """
        result = []
        for word in self.words:
            result.append(grid.findString(word))
        return list(set(result))