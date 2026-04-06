from abc import ABC, abstractmethod

class Govt(ABC):

    def __init__(self, car, salary):
        self.car = car
        self.salary = salary

    @abstractmethod
    def get_food_license(self):
        pass

class PizzaShop(Govt):

    def __init__(self, car, salary):
        Govt.__init__(self, car, salary)

    def get_food_license(self):
        return f"Applied for license"

pizzaIns = PizzaShop('Swift', 50000)
print(pizzaIns.get_food_license())