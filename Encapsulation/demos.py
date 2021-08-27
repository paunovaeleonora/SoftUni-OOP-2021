class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception('age must be greater than zero')
        self.__age = value

person = Person('Eli', 0)
print(person.age)