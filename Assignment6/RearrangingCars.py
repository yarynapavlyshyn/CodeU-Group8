class Parking:

    def __init__(self, cars):
        self._cars = cars
        self._size = len(cars)

    def cars(self):
        return self._cars.copy()

    def size(self):
        return self._size

    def rearrange(self, result):
        """
        Rearrange cars in self._cars to get the result and print out each step.
        :param result: list(int)
        :return: None or raise ValueError
        """
        if len(result) != self.size():
            raise ValueError
        if result == self._cars or not result:
            return []

        cars = self.cars()
        moves = [cars.copy()]

        car_catalog = self.catalog(self._cars)
        res_catalog = self.reversed_catalog(result)

        cars_to_move = [c for c in range(1, self._size)]

        while cars_to_move: # O(n+1) the worst case or O(n)
            # if we can place on 0's position car while it is its end position we choose the car
            car = res_catalog[car_catalog[0]] # O(1)

            if car == 0:
                car = cars_to_move[0]  # O(1)

            if res_catalog[car_catalog[car]] == car:
                cars_to_move.remove(car)  # O(1)
                continue

            cars[car_catalog[car]], cars[car_catalog[0]] = 0, car # O(1)
            car_catalog[car], car_catalog[0] = car_catalog[0], car_catalog[car] # O(1)
            moves.append(cars.copy())

        return moves

    def catalog(self, cars):
        """
        Create dictionary with numbers of cars as keys and their indices as values. Complexity is O(n)
        :param cars: list(int)
        :return: dict(int, int)
        """

        cat_dict = {}
        for i in range(self._size): # O(n)
            cat_dict[cars[i]] = i
        return cat_dict

    def reversed_catalog(self, cars):
        """
        Create dictionary with indices of cars as keys and their numbers as values. Complexity is O(n)
        :param cars: list(int)
        :return: dict(int, int)
        """

        cat_dict = {}
        for i in range(self._size): # O(n)
            cat_dict[i] = cars[i]
        return cat_dict
