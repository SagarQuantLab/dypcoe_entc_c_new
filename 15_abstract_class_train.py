from abc import ABC, abstractmethod

class Bus(ABC):

    def __init__(self, a, b):
        pass

    @abstractmethod
    def get_your_ticket(self):
        pass

class Trial(Bus):

    def __init__(self, a, b):
        Bus.__init__(self, a, b)

    def get_your_ticket(self):
        return "Hello "


trialIns = Trial(3, 4)
print(trialIns.get_your_ticket())

