from abc import abstractmethod, ABC


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_AIR_CONDITIONER_CONSUMPTION = 0.9
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = self.fuel_consumption + Car.SUMMER_AIR_CONDITIONER_CONSUMPTION
        needed_fuel = consumption * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel


    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle, ABC):
    SUMMER_AIR_CONDITIONER_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = self.fuel_consumption + Truck.SUMMER_AIR_CONDITIONER_CONSUMPTION
        needed_fuel = consumption * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)