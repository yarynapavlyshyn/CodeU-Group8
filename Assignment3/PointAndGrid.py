class Point:

    def __init__(self, grid = None, coordinates = None, value = None):
        """
        For Point initialization with optional grid and coordinates.
        :param grid: Grid
        :param coordinates: Tuple(int, int)
        :return: None
        """
        self._grid = grid
        self._coordinates = coordinates
        self._value = value
        if grid and coordinates:
            v = grid.getElement(coordinates)
            if value and value != v:
                raise ValueError
            else: self._value = v

    def getGrid(self):
        """
        Decorator for grid of the point.
        :return: Grid
        """
        return self._grid

    def getCoordinates(self):
        """
        Decorator for coordinates of the point.
        :return: tuple(int, int)
        """
        return self._coordinates

    def getValue(self):
        """
        Decorator for value of the point.
        :return: any
        """
        return self._value

    def setGrid(self, gr):
        """
        :param gr: Grid
        """
        self._grid = gr

    def setCoordinates(self, co):
        """
        :param co: Tuple(int, int)
        """
        self._coordinates = co

    def setValue(self, va):
        """
        :param va: any
        """
        self._value = va

    def __str__(self):
        """
        For string representation of Point.
        :return: string
        """
        return str(self._value)

    def __eq__(self, other):
        """
        Supports equivalence for the Point. Returns True if the elements self and other are equal, False otherwise.
        :param other: any type
        :return: bool
        """
        if isinstance(other, self.__class__):
            return self._grid == other.getGrid() and self._coordinates == other.getCoordinates() and self._value == other.getValue()
        else:
            return False

class Grid:

    def __init__(self, grid):
        """
        For Grid intialization with a grid of elements.
        :param grid: list(list())
        :return: None
        """

        self._grid = grid
        self._lowerAllElements()

    def _lowerAllElements(self):
        """
        Lower all elements in grid.
        :return: None
        """
        R, C = self.getSize()
        for r in range(R):
            for c in range(C):
                self._grid[r][c] = self._grid[r][c].lower()

    def getGrid(self):
        return self._grid

    def horizontalSize(self):
        """
        Returns number of columns. Size of a row.
        :return: int
        """
        return len(self._grid[0]) if self._grid is not None else 0

    def verticalSize(self):
        """
        Returns number of rows. Size of a column.
        :return: int
        """
        return len(self._grid) if self._grid is not None else 0

    def getElement(self, tuple):
        """
        Return an element with the given coordinates.
        :param tuple:
        :return: any type
        """
        row = tuple[0]
        col = tuple[1]
        return self._grid[row][col]

    def findElementInGrid(self, element):
        """
        Return the list of all Points with the grid and coordinates of the element if exists. None otherwise.
        :param element: any type
        :return: Point
        """
        result = []
        R, C = self.getSize()
        for r in range(R):
            for c in range(C):
                if self._grid[r][c] == element:
                    result.append(Point(self, (r, c), element))
        return result

    def findNeighborsOfPoint(self, tuple):
        """
        Return list of Points that are neighbours of element with the given coordinates.
        :param tuple: Tuple
        :return: list(Point) or None
        """
        r = tuple[0]
        c = tuple[1]
        result = []
        possible_coord = [(r-1, c-1),(r-1, c),(r, c-1),(r-1, c+1),
                          (r+1, c-1),(r+1, c),(r, c+1),(r+1, c+1)]

        for coord in possible_coord:
            if self._validCoordinates(coord):
                result.append(Point(self, coord, self.getElement(coord)))
        return result if result else None

    def ifWordInGrid(self, word):
        """
        Return True if the word can be formed in grid, False otherwise.
        :param word: str
        :return: bool
        """
        word = word.lower()
        return self.findString(word) is not None

    ############################## THE SOLUTION TO ASSIGNMENT 3 ##########################################

    def findString(self, word):
        """
        Find the word in the grid where we can starting from one position move to any neighbors,
        bub can't visit the same cell twice. Return the path if exists, None otherwise.
        :param word: string
        :return: bool
        """
        startPoints = self.findElementInGrid(word[0])
        path = []
        for startP in startPoints:
            # we are here only if the first letter of word is in grid
            path = [startP]
            path = self._findPathRecursively(startP, word, path, [])
        if self._pathIsWord(path, word):
            return path

    def _pathIsWord(self, path, word):
        if not path:
            return False
        return [p.getValue() for p in path] == list(word)

    def _findPathRecursively(self, point, word, path, visited):
        """
        Helper-function to find a word in a grid. Finds the longest path to form the word (may be only a part)
        :param point: Point
        :param word: str
        :param path: list(Point)
        :param visited: list(Point)
        :return: list(Point) or None
        """
        if self._pathIsWord(path, word):
            return path

        possible_ways = self.findPossibleWays(path, point, word, visited)
        if not possible_ways:
            # we at the same time pop the last element from path and append it to list visited
            visited.append(path.pop(-1))
            if path:
                self._findPathRecursively(path[-1], word, path, visited)

        for neighbor in possible_ways:
            path.append(neighbor)
            self._findPathRecursively(neighbor, word, path, visited)

        return path

    def findPossibleWays(self, path, point, word, visited):
        """
        Return the list of Points that can be the next element in the word.
        :return: list(Point)
        """
        neighbors = self.findNeighborsOfPoint(point.getCoordinates())
        ways = []
        for n in neighbors:
            # to not to use one Point twice -->
            if self._pathIsPartOfWord(path + [n], word) and n not in path:
                # it is of no use to go in the Point where we had been already -->
                if n not in visited:
                    ways.append(n)
        return ways

    def _pathIsPartOfWord(self, path, word):
        """
        Return True if all the elements along the path are in word respectively.
        :param path: list(Point)
        :param word: str
        :return: bool
        """
        if not path:
            return False
        valuesInPath = [point.getValue() for point in path]
        return valuesInPath == list(word)[:len(valuesInPath)]

    def _validCoordinates(self, tuple):
        """
        Return True if the given coordinates are not out of range.
        :param tuple: Tuple(int, int)
        :return: bool
        """
        numRows, numCols = self.getSize()
        if 0 <= tuple[0] < numRows and 0 <= tuple[1] < numCols:
            return True
        return False

    def getSize(self):
        """
        Two dimentional size of grid. Returns two integers: number of rows and number of columns in the grid.
        :return: int, int
        """
        return self.verticalSize(), self.horizontalSize()

    def __str__(self):
        """
        For string representation of Grid.
        :return: string
        """
        strToRet = ''
        for i in range(self.verticalSize()):
            for j in range(self.horizontalSize()):
                strToRet += str(self._grid[i][j]) + " "
            strToRet += '\n'

        return strToRet

    def __eq__(self, other):
        """
        Supports equivalence for the Grid. Returns True if the elements self and other are equal, False otherwise.
        :param other: any type
        :return: bool
        """
        if isinstance(other, self.__class__):
            return self._grid == other.getGrid()
        else:
            return False
