class papa:

    def __init__(self, car, salary):
        self.car = car
        self.salary = salary

    @staticmethod
    def my_car(salary):
        calculate_increment = salary * 1.1
        return round(calculate_increment, 1)
    
papaIns = papa('Swift', 50000)
print(papaIns.my_car(papaIns.salary))

print(papa.my_car(60000))
print(papaIns.salary)
