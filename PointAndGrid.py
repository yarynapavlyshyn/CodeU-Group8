class Point:

    def __init__(self, grid = None, coordinates = None):
        """
        For Point initialization with optional grid and coordinates.
        :param grid: Grid
        :param coordinates: Tuple(int, int)
        :return: None
        """
        self.grid = grid
        self.coordinates = coordinates

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
        row = tuple[0]
        col = tuple[1]
        return self.grid[row][col]

    def findElementInGrid(self, element):
        """
        Return the Point with the grid and coordinates of the element if exists. None otherwise.
        :param element: any type
        :return: Point
        """
        numRows, numCols = self.getSize()
        for i in range(numRows):
            for j in range(numCols):
                if self.grid[i][j] == element:
                    return Point(self, (i, j))

    def findNeighborsOfPoint(self, tuple):
        """
        Return list of Points that are neighbours of element with the given coordinates.
        :param tuple: Tuple
        :return: list(Point)
        """


    def _validCoordinates(self, tuple):
        numRows, numCols = self.getSize()
        if 0 <= tuple[0] < numRows and 0 <= tuple[1] < numCols:
            return True
        return False




    def getSize(self):
        return self.verticalSize(), self.horysontalSize()

