class Point:

    def __init__(self, grid = None, coordinates = None, value = None):
        """
        For Point initialization with optional grid and coordinates.
        :param grid: Grid
        :param coordinates: Tuple(int, int)
        :return: None
        """
        self.grid = grid
        self.coordinates = coordinates
        self.value = value

    def setGrid(self, gr):
        """
        :param gr: Grid
        """
        self.grid = gr

    def setCoordinates(self, co):
        """
        :param co: Tuple(int, int)
        """
        self.coordinates = co

    def setValue(self, va):
        """
        :param va: any
        """
        self.value = va

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.grid == other.grid and self.coordinates == other.coordinates and self.value == other.value
        else:
            return False

p1 = Point(None, (2,3),"po")
p2 = Point(None, (2,3),"po")
print(p1==p2)

class Grid:

    def __init__(self, grid):
        self.grid = grid

    def horysontalSize(self):
        """
        Returns number of columns. Size of a row.
        :return: int
        """
        return len(self.grid[0]) if self.grid is not None else 0

    def verticalSize(self):
        """
        Returns number of rows. Size of a column.
        :return: int
        """
        return len(self.grid) if self.grid is not None else 0

    def addRow(self, row):
        """
        Add a row to the grid if it is of an appropriate size, raise ValueError otherwise.
        :param row: list()
        :return: None or raise ValueError
        """
        if len(row) == self.horysontalSize():
            self.grid.append(row)
        else:
            raise ValueError("the row must be of size {}".format()) #...

    def addColumn(self, column):
        """
        Add a column to the grid (one element to each row) if it is of an appropriate size, raise ValueError otherwise.
        :param row: list()
        :return: None or raise ValueError
        """
        if len(column) == self.verticalSize():
            for row in range(self.verticalSize()):
                self.grid[row].append(column[self.verticalSize()])
        else:
            raise ValueError("the column must be of size {}".format()) #...

    def getElement(self, tuple):
        """
        Return an element with the given coordinates.
        :param tuple:
        :return: any type
        """
        row = tuple[0]
        col = tuple[1]
        return self.grid[row][col]

    def findElementInGrid(self, element):
        """
        Return the Point with the grid and coordinates of the element if exists. None otherwise.
        :param element: any type
        :return: Point
        """
        result = []
        numRows, numCols = self.getSize()
        for i in range(numRows):
            for j in range(numCols):
                if self.grid[i][j] == element:
                    result.append(Point(self, (i, j)))

    def findNeighborsOfPoint(self, tuple):
        """
        Return list of Points that are neighbours of element with the given coordinates.
        :param tuple: Tuple
        :return: list(Point)
        """
        row = tuple[0]
        col = tuple[1]
        result = []
        possible_coord = [(row-1, col-1),(row-1, col),(row, col-1),(row-1, col+1),
                          (row+1, col-1),(row+1, col),(row, col+1),(row+1, col+1)]
        for coord in possible_coord:
            if self._validCoordinates(coord):
                result.append(Point(self, coord, self.getElement(coord)))
        return result

    def findString(self, word):
        """
        Find the word in the grid where we can starting from one position move to any neighbors,
        bub can't visit the same cell twice.
        :param word: string
        :return: bool
        """
        path = []
        '''
        startPoints = self.findElementInGrid(word[0])
        for startP in startPoints: # we go further only if the first letter of word is in grid
            neighbors = self.findNeighborsOfPoint(startP.coordinates)
            i = 1
            while True:
                for
        '''

        return path

    def _validCoordinates(self, tuple):
        """
        Return True if the given coordinates are not out of range.
        :param tuple: Tuple(int, int)
        :return:
        """
        numRows, numCols = self.getSize()
        if 0 <= tuple[0] < numRows and 0 <= tuple[1] < numCols:
            return True
        return False

    def getSize(self):
        """
        Return two integers: number of rows and number of columns in the grid.
        :return: int, int
        """
        return self.verticalSize(), self.horysontalSize()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.grid == other.grid
        else:
            return False