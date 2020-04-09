class Car_lot():
    def __init__(self, address, number_of_floors, day_price, total_spots):
        self.address = address
        self.number_of_floors = number_of_floors
        self.day_price = day_price
        self.hour_price = hour_price
        self.__total_spots = total_spots

    """Total number of spots is protected"""


def get_total_spots(self):
    return self.__total_spots


def number_of_free_spots():
    pass
