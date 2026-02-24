'''
Built in function are fuctions that exists by default
print()
len()
int()
float()
input()
round()
abs()
min()
max()
sum()
str()
range()
'''

#print function displays the provided input
print('Hello','World','2026','learning python', [1, 2, 3, 4], True)

#len() : It returns the length of the input
print(len('cat'))
print(len('Finland'))
print(len('cat dog'))
print(len([1, 2, 3]))
print(len({1, 2, 3}))
print(len({1, 2, 2, 3, 3}))

Firstname = 'Brigette'
Lastname = 'Yeo'
age = 250
hobby = 'rock climbing'
country = 'Finland'

fullname = (Firstname + ' ' + Lastname)

print(f'I am {fullname}, I am {age} years old this year. I live in {country} now and my favourite hobby is {hobby}.')
print('My name is {0}. I live in {1} and I am {2} years old. {1} is beautiful.'.format(fullname, country, age))

print(10, '10')
print(type(10), type('10'), int('10'), type(int('10')))

print(str(10) + '10')
print(10 + int('10'))

print('9.81', type('9.81'))
print(float('9.81'), type(float('9.81')))
print(float('9.81') * 100, int(float('9.81') * 100))

""" current_year = 2026
name = input('Enter your name: ')
birth_year = int(input('Enter your birth year: '))
print(name, current_year, birth_year, type(birth_year))
age = current_year - birth_year

print(f'You are {name}. You were born in {birth_year}. Now, you are {age} years old.') """

mass = 75.5
gravity = 9.81 
weight = mass * gravity 

print(weight, round(weight), round(weight, 2))
print(abs(-10))
print(min(10, 20, -10, 0, 30, 21))
print(max(10, 20, -10, 0, 30, 21))
print(sum([10, 20, -10, 0, 30, 21]))

print(list())
print(list('cat'))
print(list({1, 2, 3, 4, 5}))

print()

even_numbers = list(range(0, 101, 2))
print(even_numbers)

odd_numbers = list(range(1, 101, 2))
print(odd_numbers)