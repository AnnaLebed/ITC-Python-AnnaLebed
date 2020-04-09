from Vehicle import *


class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        """Attributes specific to the class car"""
        self.transmission = transmission
        """Protected attribute: car number"""
        self.__car_number = car_number

    def get_car_number(self):
        return self.__car_number

    def car_description(self):
        description = self.make + ' ' + self.model + ', ' + "year " + str(self.year)
        return description.title()

    def describe_transmission(self):
        print("This car has " + self.transmission + " transmission")

    def drive(self):
        print("The car is moving")

    def parking(self):
        print("The car is parked")


my_car = Car('audi', 'a4', 2020, "red")
print(my_car.car_description())


class Bike(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        """Attributes specific to bikes: type (mechanical or electrical)"""
        self.type = type
        """Protected data"""
        self.__owner_id = owner_id

    def get_owner_id(self):
        return self.__owner_id

    def drive(self):
        print("The bike is moving")


    def parking(self):
        print("The bike is parked")
