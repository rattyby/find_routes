class Car:
    """ Класс транспортного средства Легковой автомобиль. """
    def __init__(self, patency=3, consumption=10):
        """ Инициализация объекта Car. """
        self.patency = patency
        self.consumption = consumption


class Truck(Car):
    """ Класс транспортного средства Грузовой автомобиль, наследник класса Car. """
    def __init__(self, patency=2, consumption=12):
        """ Инициализация объекта Truck через метод предка. """
        super().__init__(patency, consumption)


class Bus(Car):
    """ Класс транспортного средства Автобус, наследник класса Car. """
    def __init__(self, patency=1, consumption=15):
        """ Инициализация объекта Bus через метод предка. """
        super().__init__(patency, consumption)


class Suv(Car):
    """ Класс транспортного средства Внедорожник, наследник класса Car. """
    def __init__(self, patency=6, consumption=18):
        """ Инициализация объекта Suv через метод предка. """
        super().__init__(patency, consumption)
