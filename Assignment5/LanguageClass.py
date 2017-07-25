
# Recursive finding of alphabet. In each updating of the graph we deal with only first letters.
# If the letters are the same we create a new Language with this words with the same first letter
# but without removing it.
# Then we use this graph to create a language.


class Language:

    def __init__(self, words):
        """ For Language initialization with a list of "sorted" words. """
        # to remove empty strings
        self._words = [w for w in words if w]  # O(n)
        self._alphabet = [] # O(1)
        self.generate_alphabet()

    def alphabet(self):
        """ Decorator for self._alphabet. """
        return self._alphabet # O(1)

    def words(self):
        """ Decorator for self._words. """
        return self._words # O(1)

    def _fill_alphabet(self):
        self._alphabet = []
        for word in self._words:  # n times
            for letter in word:  # l times (where l is mean length of words)
                if letter not in self._alphabet:
                    self._alphabet.append(letter) # total: O(n*l)

    def _fill_graph(self):
        """
        Create dictionary with all the letters self._words are created with as keys and empty
        sets as values.
        :return: dict(str, str)
        """
        self._alphabet = []
        graph = {} # O(1)
        for word in self._words: # n times
            for letter in word: # l times (where l is mean length of words)
                if letter not in graph:
                    graph[letter] = set()   # total: O(n*l)
                    self._alphabet.append(letter)
        return graph

    ######### GENERATE GRAPH WITH "VERTICES" (letters) AND "EDGES" (from the letters to their righter letters) #########

    def _generate_graph(self):
        """
        Generate graph with all letters as keys and letters that are righter then each of each of them in alphabet.
        :return: dict(str, str)
        """
        # in graph a node from l1 to l2 mean that l2 is righter than l1: [..., l1, ...,  l2, ...]
        graph_with_letters = self._fill_graph() # O(n*l)
        graph = self._update_graph_rec(graph_with_letters, self) # O(n^2) in the worst case
        return graph

    def _update_graph_rec(self, graph_with_letters, language):
        """
        Recursive function that gets the language and graph to update, add to the graph first letters in the
        language words. If the letters are he same finds a new language and call the function for it recursively.
        :param graph_with_letters: dict(str, str)
        :param language: Language
        :return: dict(str, str)
        """
        # O(n) where n is number of elements in language
        if not language.words():
            return graph_with_letters

        first_letters = [w[0] for w in language.words()]  # O(n)
        graph_with_letters = self._update_graph_with_first_letters(first_letters, graph_with_letters)

        new_lang_words = [language.words()[0][1:]] # O(l) where l is length of first word in language words
        i = j = 0
        while True:
            j += 1
            if j > len(first_letters) - 1:
                if new_lang_words and len(new_lang_words) > 1:
                    self._update_graph_rec(graph_with_letters, Language(new_lang_words))
                break
            letter = first_letters[i]
            next_letter = first_letters[j]

            if letter == next_letter:
                new_lang_words = self._update_new_lang_word(language, new_lang_words, j) # O(1)
            else:
                if len(new_lang_words) > 1:
                    graph_with_letters = self._update_graph_rec(graph_with_letters, Language(new_lang_words))
                new_lang_words = self._update_new_lang_word(language, new_lang_words, j, True) # O(1)
            i += 1
        return graph_with_letters

    def _update_graph_with_first_letters(self, first_letters, graph):
        """
        Add all elements in first_letters to the dictionary in terms
        :param first_letters: list(str)
        :param graph: dictionary(str, str)
        :return: dictionary(str, str)
        """
        i = 1
        for let in first_letters:  # (n) times
            # (n-1)+(n-2)+(n-3)+(n-4)+…+(n-n) = n^2–(1+2+3+…+n) = n^2–(n+1)*n/2 = 2n2– n2–n)/2 = (n-1)*n/2 -->
            for j in range(i, len(first_letters)):  # (n-1)*n/2 times
                righter_let = first_letters[j]
                if righter_let != let and righter_let not in graph[let]:  # O(1)
                    graph[let].add(righter_let)  # O(1)
            i += 1
        return graph

    def _complete_graph(self, graph):
        """
        Add edge to graph if not exists but the path from one vertex to another does exist.
        :param graph: dict(str, str)
        :return: dict(str, str)
        """
        for key_letter in graph:
            new_values = graph[key_letter].copy()
            for value_letter in new_values:
                graph[key_letter].update(graph[value_letter])
        return graph

    def _update_new_lang_word(self, lang, new_lang_words, j, to_create_new = False):
        """
        Helper function that update list of words with a new word (j-th in lang words) to create
        then a new language with them.
        :param lang: Language
        :param new_lang_words:list(str)
        :param j: int
        :param to_create_new: bool
        :return: list(str)
        """
        # O(1)
        new_word = lang.words()[j][1:]
        if not new_word:
            return []
        if to_create_new:
            return [new_word]
        else:
            new_lang_words.append(new_word) # O(n)
            return new_lang_words

    def _sort_alphabet_using_graph(self, graph):
        """
        Sort the self._alphabets using the graph and its properties (values of each key are righter letters).
        :return: None
        """
        alfabet = self._alphabet
        for key_letter in graph:
            indices = [alfabet.index(value_letter) for value_letter in graph[key_letter]]
            i = min(indices) if indices else len(alfabet) - 1
            alfabet.remove(key_letter)
            alfabet.insert(i, key_letter)
        self._alphabet = alfabet

    def generate_alphabet(self):
        """
        Create alphabet using other methods - update self._alphabet
        :return: None
        """
        self._fill_alphabet()
        graph = self._generate_graph()
        graph = self._complete_graph(graph)
        self._sort_alphabet_using_graph(graph)