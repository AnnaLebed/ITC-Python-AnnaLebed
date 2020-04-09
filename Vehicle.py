class Vehicle():

    def __init__(self, make, model, year, color):
        """Initialize vehicle attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The vehicle is moving")

    def parking(self):
        print("The vehicle is parked")
