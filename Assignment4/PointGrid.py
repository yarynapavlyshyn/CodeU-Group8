class Grid:

    def __init__(self, grid):
        """
        For grid initialization with a grid with elements.
        :param grid: list(list(any))
        :return: None
        """
        self._grid = grid
        self._points = {}
        self._update_points()
        self._islands = []

    class Point:
        def __init__(self, value, coordinates):
            self.coordinates = coordinates
            self.value = value
            self.is_visited = False

        def visit(self):
            """
            Set the visit attribute to be True.
            :return: None
            """
            self.is_visited = True

        def __eq__(self, other):
            """
            Supports equivalence for the Point. Returns True if the elements self and other are equal, False otherwise.
            :param other: any
            :return: bool
            """
            if isinstance(other, self.__class__):
                return self.coordinates == other.coordinates and self.value == other.value and self.is_visited == other.is_visited
            else:
                return False

    def find_point(self, point_value):
        """
        Return the first NOT VISITED Point in self._points with the given value if exists. None otherwise.
        :param point_value: any
        :return: Point or None
        """
        for coord in self._points:
            point = self.get_point(coord)
            if point.value == point_value and point.is_visited == False:
                return point

    def get_point(self, coordinates):
        """
        Get element in Grid by its coordinates. Raises ValueError if coordinates are invalid.
        :param coordinates: tuple(int,int)
        :return: Point or raise ValueError
        """
        if not self.valid_coordinates(coordinates):
            raise ValueError("invalid coordinates")
        return self._points[coordinates]

    def get_element(self, coordinates):
        """
        Return element in the Grid by its coordinates.
        :param coordinates: tuple(int, int)
        :return: any
        """
        return self._grid[coordinates[0]][coordinates[1]]

    def valid_coordinates(self, coordinates):
        """
        Check if the coordinates are valid. Return True if so, False otherwise.
        :param coordinates: tuple(int, int)
        :return: bool
        """
        Rs, Cs = self.size()
        return coordinates[0] in range(0, Rs) and coordinates[1] in range(0, Cs)

    def _find_neighbor_land(self, point):
        """
        Returns a list of all neighbors of the point that are 'land'.
        :param point: Point
        :return: list(Points)
        """
        Rs, Cs = self.size()
        r, c = point.coordinates[0], point.coordinates[1]

        possible_coordinates = [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]
        return [self.get_point(coo) for coo in possible_coordinates
                if (self.valid_coordinates(coo) and self.is_land(coo))]

    def is_land(self, coordinates):
        """
        Return True if cell with such a coordinates is land - the value is 'T', False otherwise.
        :param coordinates: tuple(int, int)
        :return: bool
        """
        return self.get_element(coordinates) == 'T'

    def find_land(self):
        """
        Find all the points that have value 'T' and return them in a list.
        :return: list[Points]
        """
        land = [self.get_point(coo) for coo in self._points if self.is_land(coo)]
        return land if land else None

    ################################# FIND ISLANDS HERE ###########################################

    '''
    We find islands as lists of coordinates just to make it easier to test and to print them out.
    If you find it better to have them as list of Points just replace "island.append(point.coordinates)"
    in _recursive() with "island.append(point)".
    '''

    def find_islands(self):
        """
        Find islands in a grid and return a list of lists of points
        :return: list(list(tuple(int,int))) or None
        """
        land = self.find_land()
        if not land:
            return
        self._islands = []
        for p in land:
            if not p.is_visited:
                self._islands.append(self._recursive(p,[]))

        return self._islands if self._islands else None

    def _recursive(self, point, island):
        """
        Helper function that find island that contains the given point and return as a list of coordinates.
        :param point: Point
        :return: list(tuple(int,int))
        """
        island.append(point.coordinates)
        point.visit()
        ways = self._find_neighbor_land(point)
        for p in ways:
            if not p.is_visited:
                self._recursive(p, island)
        return island

    def size(self):
        """
        Return number of rows and of columns in the Grid.
        :return: int, int
        """
        return len(self._grid), len(self._grid[0])

    def _update_points(self):
        """
        Update a dictionary self._points with coordinates as keys and Point with the coordinates
        as values in the Grid.
        :return: None
        """
        Rs, Cs = self.size()
        for r in range(Rs):
            for c in range(Cs):
                self._points[(r, c)] = (self.Point(self._grid[r][c], (r, c)))

    def __str__(self):
        """
        For string representation of Grid. It is supposed that each element is one character length.
        :return: str
        """
        result = ''
        for row in self._grid:
            for element in row:
                result += str(element) + ' '
            result += '\n'
        return result
