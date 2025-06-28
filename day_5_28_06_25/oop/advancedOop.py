# Inheritance, super(), Encapsulation
class Vehicle:
    def __init__(self, brand, year, mileage): # any method surronded by __  is pre-defined by python and allows to customazible
        self._brand = brand
        self._year = year
        self.__mileage =mileage

    def start(self):
        print('vehicle started')

    def stop(self):
        print('vehicle stopped')

    def get_mileage(self):
        return self.__mileage

    def display_info(self):
        print('brand of the vehicle', self._brand)
        print('manufactured year of the vehicle', self._year)

class Car(Vehicle): # Inheritence => all methods including special methods are inherited to Class Car
    def __init__(self, brand, year, mileage, model, num_doors):
        super().__init__(brand, year, mileage)  # super() keyword calls
        self.model =model
        self.num_doors = num_doors

    def start(self): # method over-ride
        print('Car Engine started')

    def display_info(self): # using parent display_info and adding additional info
        super().display_info()
        print('Model:', self.model)
        print('num_doors', self.num_doors)

class Bike(Vehicle): #Inheritance
    def __init__(self, brand, year, mileage, typee):
        super().__init__(brand, year, mileage)
        self.typee = typee

    def start(self):# method over-ride
        print('Bike Ignition On')

    def display_info(self): # using parent display_info and adding additional info
        super().display_info()
        print('type of bike', self.typee)


c = Car('hyundai', '2025', '19 kmpl', 'Creta',5)
c._brand = 'kia' # accessng the protected attribute and changing it
# name mangling for private variables. python for private attributes stores lik _className__variable can be used to update private and works but not recommended
c._Vehicle__mileage = 50 # accessng private attribute and changing it not recommended
c.display_info()
print('mileage', c.get_mileage())
c.start()
c.stop()

b = Bike('KTM', 2025, 30, 'sports')
b.display_info()
print('mileage', b.get_mileage())
b.start()
b.stop()

# polymorphism

class Dog:
    def sound(self):
        print('bow bow')

class Cat:
    def sound(self):
        print('mew mew')

i = [Dog(),Cat()] # two class initialization assigned to one

for type in i:
    type.sound() # iteratng over call teh sound method of both class depending on type of class instance sound changes eventhough both class have same name




