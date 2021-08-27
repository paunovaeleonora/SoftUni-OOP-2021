from project2.customer import Customer
from project2.equipment import Equipment
from project2.exercise_plan import ExercisePlan
from project2.subscription import Subscription
from project2.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_object(oid, cls_iterable):
        return list(filter(lambda _: _.id == oid, cls_iterable))[0]

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return False
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return False
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return False
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return False
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return False
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        current_subscription = self.get_object(subscription_id, self.subscriptions)
        customer_id = current_subscription.customer_id
        customer = self.get_object(customer_id, self.customers)
        trainer_id = current_subscription.trainer_id
        trainer = self.get_object(trainer_id, self.trainers)
        current_plan = self.get_object(trainer_id, self.plans)
        current_equipment = self.get_object(current_plan.equipment_id, self.equipment)
        return f'{current_subscription}\n{customer}\n{trainer}\n{current_equipment}\n{current_plan}'


# customer = Customer('John', 'Maple Street', 'john.smith@gmail.com')
# equipment = Equipment('Treadmill')
# trainer = Trainer('Peter')
# subscription = Subscription('14.05.2020', 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
# gym = Gym()
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
# print(Customer.get_next_id())
# print(gym.subscription_info(1))
