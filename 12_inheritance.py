class Papa:

    def __init__(self, car, salary_amount):
        self.car = car
        self.amount = salary_amount

    def __salary_details(self):
        return f"My salary is {self.salary_details}"
    
    def _my_car(self):
        return f"Run my car {self.car}"
    

class rohan(Papa):

    def __init__(self, car, salary_amount, my_salary):
        Papa.__init__(self, car, salary_amount)
        self.my_salary = my_salary

    def run_papa_car(self):
        return self._my_car()
    
    def access_papa_salary(self):
        return self.__salary_details()
    
    def __my_salary(self):
        return self.my_salary
    

class sohan(rohan):

    def __init__(self, car, salary_amount, my_salary):
        rohan.__init__(self, car, salary_amount, my_salary)
    
    def access_granpa_car(self):
        return self._my_car()
    
    def access_rohan_salary(self):
        return self.__my_salary()


# instanceRohan = rohan('Baleno', 50000)
# print(instanceRohan.run_papa_car())
# # print(instanceRohan.__salary_details())
# print(instanceRohan.access_papa_salary())

instanceSohan = sohan('Baleno', 50000, 80000)
print(instanceSohan.access_granpa_car())
print(instanceSohan.access_rohan_salary())