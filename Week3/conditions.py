a = 3
condition = a > 0
print(condition)
if condition:
    print('The number is positive')
else:
    print('This is the plan B')

#another example
a = 3

if a > 0:
    print(f'{a} is positive')
elif a == 0:
    print(f'{a} is a zero')
else:
    print(f'{a} is negetive')


#Weather

is_raining = True

if is_raining == True:
    print('Go out with umbrella')
else:
    print('Go out freely')

weather = 'rainy'

if weather == 'rainy':
    print('Go out with raincoat')
elif weather == 'sunny':
    print('Just go out freely it is sunny')
elif weather == 'cloudy':
    print('Might be rainy later')
elif weather == 'snowy':
    print('Might be slippery')
elif weather == 'foggy':
    print('Might have visibility issues')
else:
    print('No one knows about today weather')   

#input example
weather = input('What is the weather today?').lower()
print(weather)

if weather == 'rainy':
    print('Go out with raincoat')
elif weather == 'sunny':
    print('Just go out freely it is sunny')
elif weather == 'cloudy':
    print('Might be rainy later')
elif weather == 'snowy':
    print('Might be slippery')
elif weather == 'foggy':
    print('Might have visibility issues')
else:
    print('No one knows about today weather')   


