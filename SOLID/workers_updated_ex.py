from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        raise NotImplementedError()


class EatMixin(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError()


class Worker(AbstractWorker, EatMixin):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker, EatMixin):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)
        self.worker = worker


class WorkManager(Manager):
    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorker, EatMixin):
    def work(self):
        print("I'm a robot. I'm working....")

    def eat(self):
        return "I don't need to eat..."


manager = Manager()
manager.set_worker(Worker())
manager.manage()
manager.lunch_break()
manager.set_worker(SuperWorker())
manager.manage()
manager.lunch_break()
manager.set_worker(Robot())
manager.manage()
manager.lunch_break()



# Може би eat да не е abstracten в бащиния клас.
# Също може да се създадат два отделни класа,
# един абстрактен с work и втори наследяващ първия и разширяващ с eat
