# Arithematic operators
# from day2.pythonCollections import personalDetails, coordinates

a = 10
b = 20
print(a+b) # addition
print(a-b) # subtraction
print(a*b) #multiplication
c =b/a # division
print(a/b)
print(c)
print(type(c))
print(a//b) # Floor division
print(b//a)
print(a%b) # Modulus operator
print(b%a)
print(a**2) #power

# comparison operators
print('####comparison operators####')
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

# logical operator
print('####logical####')
print(a<b and a!=b)
print(a<b or a>b)
print(not a<b)

# Assignment operators
print("#### Assignment Operators ####")
a+=b # a=a+b
print(a)
a-=b # a=a-b
print(a)
a*=b # a=a*b
print(a)
a/=b # a=a/b
print(a)
a**=b # a= a**b
print(a)
print(type(a))
a//=b
print('floor',a)
a%=b
print('modulus',a)

# Identity Operators
print('####Identity####')
c=[1,2,3]
d=[1,2,3]
e=c
print('###is###')
print(c is d) # compares the c and d are pointing to same object
print(e is c)
print('###is not###')
print(c is not d)
print(e is not c)

# Membership Operators list, dict, string or set, tuple
print('####Membership####')
fruits=["banana", "mango", "pine","apple"]
personalDetails = {
    "name":"Renuka",
    "age": 27
}
name='REnukaPrasad'
noDuplicate = {"ferrari","mercedes", "volvo"}
coordinates = (10,220)
print('###in###')
print("banana" in fruits)
print("age" in personalDetails) # in dic 'in' checks only for keys not value
print('P' in name) # 'in' case sentive in string
print("benz" in noDuplicate)
print('###not in###')
print("banana" not in fruits)
print("age" not in personalDetails) # in dic 'in' checks only for keys not value
print('P' not in name) # 'in' case sentive in string
print("benz" not in noDuplicate)
print('##tuple##')
print( 10 in coordinates)
print(20 not in coordinates)
multipleCoordinates = ((10,220), (12,20))
print((10,220)  in multipleCoordinates)


