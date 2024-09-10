#from single to multiple Inheritance
class Building():
    def __init__(self):
        pass
class Cathedral(Building):
    def __init__(self):
        super().__init__()

trp = Cathedral()
print(trp)