from wild_cat.customer import Customer
from wild_cat.dvd import DVD


class MovieWorld(Customer, DVD):
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        searched_customer = [c for c in self.customers if c.id == customer_id]
        searched_dvd = [d for d in self.dvds if d.id == dvd_id]
        if searched_dvd:
            if searched_dvd[0] in searched_customer[0].rented_dvds:
                if searched_dvd[0].is_rented():
                    return f'{searched_customer[0].name} has already rented {searched_dvd[0].name}'
            else:
                if searched_dvd[0].is_rented:
                    return 'DVD is already rented'
            allowed_age = searched_dvd[0].age_restriction
            customer_age = searched_customer[0].age
            if allowed_age > customer_age:
                return f'{searched_customer[0].name} should be at least {allowed_age} to rent this movie'
            searched_customer[0].rented_dvds.append(searched_dvd[0])
            searched_dvd[0].is_rented = True
            return f'{searched_customer[0].name} has successfully rented {searched_dvd[0].name}'

    def return_dvd(self, customer_id, dvd_id):
        s_customer = [c for c in self.customers if c.id == customer_id]
        searched_dvd = [dvd for dvd in s_customer[0].rented_dvds if dvd.id == dvd_id]
        if searched_dvd:
            returned_dvd = searched_dvd[0].name
            searched_dvd[0].is_rented = False
            s_customer[0].rented_dvds.remove(searched_dvd[0])
            return f'{s_customer[0].name} has successfully returned {returned_dvd}'
        return f'{s_customer[0].name} does not have that DVD'

    def __repr__(self):
        customers = [c.__repr__() for c in self.customers]
        dvds = [d.__repr__() for d in self.dvds]
        details = '\n'.join(customers)
        if dvds:
            details += '\n' + '\n'.join(dvds)
        return details


# c1 = Customer('John', 16, 1)
# c2 = Customer('Anna', 55, 2)
# d1 = DVD('Black Widow', 1, 2020, 'April', 18)
# d2 = DVD.from_date(2, 'The Croods 2', '23.12.2020', 3)
# movie_world = MovieWorld('The Best Movie Shop')
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
# print(movie_world)

