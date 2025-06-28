#problem statement
#
#  Create a class called Car with:

# Attributes: brand, model, year

# Method: display_info() that prints car details

class Car:
    # A special method called when an object is created or constructor
    # self is the first attribute inside methods
    def __init__(self, brand, model, year):
        self.brand =brand
        self.model = model
        self.year = year
    # method 1
    def display_info(self):
        print('Brand of the Car is =', self.brand)
        print('Model of the car is =',self.model)
        print('Manufactured year is =', self.year)
    # method 2
    def recommended(self):
        match self.brand:
            case 'altroz':
                print('it is recommended to buy')
            case _:
                print('doesn\'t match with anyone of the good recommended model')


# creating instace of the Car class
c = Car('altrozv','xyz','2025')
# accessing the attribute of a class and changing it
c.brand ='non'
# accessing the methods in class using instances

c.display_info()
c.recommended()
