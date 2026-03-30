# # CLASS DEFINITION
# class myCar:
#     pass

# # CALLING OF CLASS
# myCar()

class myCar:

    def __init__(self, name, maker):
        self.name = name
        self.maker = maker

carInstance = myCar('Maruti', 'Baleno')
print(carInstance.maker, carInstance.name)