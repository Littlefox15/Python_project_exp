'''
Docstring for Day1.data_types

Number: (integer, float, complex), examples: 10, 9.8, 4 +2j
String: Any text under single, double or triple quote
Boolean: Their value is either True or False
List: indexed and ordered list of items, eg [1,2,3], [Finland, Sweden, Norway]
Set: Set is a collection of unique items.
A= {1, 2, 3, 4, 5}
B= {5, 8, 9, 3, 4}
Tuple: an order collection of items which is immutable
A = (1, 2, 3, 4)
'''

#String example
txt ='Name: Brigette'
print( txt )

 
a = 10        # int
b = 3.14       # float
c = 4 - 7j    # complex

print(a, type(10))          # Int
print(b, type(3.14))        # Float
print(c, type(4 - 7j))      # Complex number

#Area of land
Length = 20
Width = 15
Area = (Length * Width)
print(f'The area of the land is {Area}m^2')

#Weight
gravity = 9.81
mass = 450
weight = (mass * gravity)
print(f'The gravity of the body is {weight} Newton on planet Earth.')

#BMI
mass = 45
height = 1.51
BMI = (mass / (height**2))
print(f'My BMI is {BMI}.')