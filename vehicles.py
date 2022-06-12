class Car:
    def __init__(self, patency=3, consumption=10):
        self.patency = patency
        self.consumption = consumption


class Truck(Car):
    def __init__(self, patency=2, consumption=12):
        super().__init__(patency, consumption)


class Bus(Car):
    def __init__(self, patency=1, consumption=15):
        super().__init__(patency, consumption)


class Suv(Car):
    def __init__(self, patency=6, consumption=18):
        super().__init__(patency, consumption)
