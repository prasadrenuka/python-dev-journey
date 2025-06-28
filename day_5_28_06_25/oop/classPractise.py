#  Create a class called Car with:

# Attributes: brand, model, year

# Method: display_info() that prints car details

class Car:
    def __init__(self, brand, model, year):
        self.brand =brand
        self.model = model
        self.year = year
    def display_info(self):
        print('Brand of the Car is =', self.brand)
        print('Model of the car is =',self.model)
        print('Manufactured year is =', self.year)
    def recommended(self):
        match self.brand:
            case 'altroz':
                print('it is recommended to buy')
            case _:
                print('doesn\'t match with anyone of the good recommended model')


# creating instace of the Car class
c = Car('altrozv','xyz','2025')
# accessing the method in class
c.display_info()
c.recommended()
