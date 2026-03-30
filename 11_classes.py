# # CLASS DEFINITION
# class myCar:
#     pass

# # CALLING OF CLASS
# myCar()

class myCar:

    def __init__(self, name, maker):
        self.name = name
        self.maker = maker
        self.greetFunction()

    def greetFunction(self):
        return f"Hello {self.name} from {self.maker}"
    
    def car_details(self, cc):
        return f"Hello this is {self.name} from {self.maker} which has a capacity of {cc}"

carInstance = myCar("Baleno", "Maruti")
print(carInstance.greetFunction())
print(carInstance.car_details('1500cc'))
