from wild_cat.animals.animal import Mammal
from wild_cat.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Fruit, Vegetable]
        self.weight_per_food = 0.1

    def make_sound(self):
        return f'Squeak'


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.4

    def make_sound(self):
        return f'Woof!'


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat, Vegetable]
        self.weight_per_food = 0.3

    def make_sound(self):
        return f'Meow'


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 1

    def make_sound(self):
        return f'ROAR!!!'
