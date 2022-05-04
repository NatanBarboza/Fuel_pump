class FuelPump:
    def __init__(self, type_fuel:str, value:float):
        self.__type_fuel = type_fuel
        self.__value = value
        self.__fuel_quantity = 1000

    @property
    def type_fuel(self):
        return self.__type_fuel

    @type_fuel.setter
    def type_fuel(self, new_type):
        self.__type_fuel = new_type

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def fuel_quantity(self):
        return self.__fuel_quantity

    @fuel_quantity.setter
    def fuel_quantity(self, new_quantity):
        self.__fuel_quantity = new_quantity

    def to_fuel(self, value):
        total = value / self.__value
        self.__fuel_quantity = self.__fuel_quantity - total

        total_brl = total * self.__value

        return total, total_brl

    def fuel_per_l(self, value):
        total = value * self.__value
        self.__fuel_quantity = self.__fuel_quantity - value

        total_l = total / self.__value

        return total, total_l