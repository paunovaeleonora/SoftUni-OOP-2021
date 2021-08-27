class Person:
    def __init__(self, name, age,):
        self.name = name
        self.age = self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('Age cannot be negative')
        return age


class Employee(Person):
    def __init__(self, name, age, date):
        super().__init__(name, age)
        self.date = date


class Manager(Person):
    def __init__(self, name, age, people_managing):
        super().__init__(name, age)

        self.people_managing = people_managing


class Contractor(Person):
    def __init__(self, name, age, date_of_expiry):
        super().__init__(name, age)
        self.date_of_expiry = date_of_expiry


e = Employee('test', -5, '2020-02-10')
