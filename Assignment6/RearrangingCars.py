import random


class Parking:

    def __init__(self, cars):
        self._cars = cars
        self._size = len(cars)

    def cars(self):
        return self._cars

    def size(self):
        return self._size

    def rearrange(self, result):
        """
        Rearrange cars in self._cars to get the result and print out each step.
        :param result: list(int)
        :return: None
        """
        cars = self._cars
        moves = []

        car_catalog = self.catalog(self._cars)
        res_catalog = self.catalog(result)

        cars_to_move = [c for c in range(1, self._size)]

        while cars_to_move:

            car = random.choice(cars_to_move)  # O(n)
            if car_catalog[car] == res_catalog[car]:
                cars_to_move.remove(car) # O(1)
                continue

            moves.append(cars.copy())

            cars[car_catalog[car]], cars[car_catalog[0]] = 0, car # O(n)

            car_catalog[car], car_catalog[0] = car_catalog[0], car_catalog[car] # O(1)

        moves.append(cars)
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

Park = Parking([1, 2, 0, 3])
moves = Park.rearrange([1, 3, 0, 2])

for i in moves:
    print(i)