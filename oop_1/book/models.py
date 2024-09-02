class Car:
    def __init__(self, model, number, color="Black", fuel=50, full_tank=50):
        self.model = model
        self.number = number
        self.color = color
        self.fuel = fuel
        self.full_tank = full_tank
        print("starting a new car")

    def __str__(self):
        return f"model:{self.model}"
