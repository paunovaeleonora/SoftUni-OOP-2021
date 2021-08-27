class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class CarTestCase(TestCase):
    def setUp(self):
        self.car = Car('V', 'SRI', 5, 40)

    def test_constructor(self):
        self.assertEqual('V', self.car.make)
        self.assertEqual('SRI', self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(40, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_property_make(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        self.car.make = "Vauxhall"
        self.assertEqual('Vauxhall', self.car.make)

    def test_property_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
        self.car.model = "SR"
        self.assertEqual('SR', self.car.model)

    def test_property_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        self.car.fuel_consumption = 4
        self.assertEqual(4, self.car.fuel_consumption)

    def test_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        self.car.fuel_capacity = 50
        self.assertEqual(50, self.car.fuel_capacity)

    def test_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

        self.car.refuel(50)
        self.assertEqual(40, self.car.fuel_amount)

    def test_drive(self):
        car = Car('V', 'SRI', 5, 40)
        self.assertEqual('V', car.make)
        self.assertEqual('SRI', car.model)
        self.assertEqual(5, car.fuel_consumption)
        self.assertEqual(40, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

        car.refuel(10)
        self.assertEqual(10, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.drive(300)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

        car.drive(200)
        self.assertEqual(0, car.fuel_amount)


if __name__ == "__main__":
    main()