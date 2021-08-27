from wild_cat.animals.animal import Bird
from wild_cat.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.25

    def make_sound(self):
        return f'Hoot Hoot'


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Meat, Vegetable, Fruit, Seed]
        self.weight_per_food = 0.35

    def make_sound(self):
        return f'Cluck'
