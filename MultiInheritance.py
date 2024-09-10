#from single to multiple Inheritance
class Building():
    def __init__(self, walls, doors, windows):
        self.walls = walls
        self.doors = doors
        self.windows = windows
    def building_info(self):
        return self.walls, self.doors, self.windows
    def show_building(self):
        print('Walls: {}, Doors: {}, Windows: {}'.\
            format(*self.building_info()))  #unpack tuple using star* syntax

class SpaceShip():
    def __init__(self, destination):
        self.destination = destination
    def show_spaceship(self):
        print('flying', self.destination)
class Art():
    def __init__(self, type_of = '[unknown]'):
        self.art_type = type_of
    def show_art(self):
        print('Our Art is a {}'.format(self.art_type))

class MixIn():
    def print_dict(self, class_instance):
        print(class_instance.__dict__)          #print dict of the object

class Cathedral(Building,SpaceShip,Art,MixIn):
    def __init__(self, destination, walls=4, doors =1, windows= 2):
        super().__init__(walls,doors,windows)   #first super call first/left hand inherited class
        SpaceShip.__init__(self, destination)   #second init we name the parent class
        Art.__init__(self, type_of='cathedral')
        MixIn().print_dict(self)

class Cafe(Building, MixIn):   #multiple inheritance using a mix-in
    def __init__(self, name):
        super().__init__(walls=4, doors=2, windows=6)
        print(name)
        MixIn().print_dict(self)

trp = Cathedral(windows=1000, destination='keo')
trp.show_art()
trp.show_spaceship()
trp.show_building()
print()
java_house = Cafe('the ke')