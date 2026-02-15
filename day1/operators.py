# Day 1 - 30DaysOfPython Challenge
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print('the remainder is', 7 % 2)             # modulus(%)
print('the quotient is', 7 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(4 - 5j))      # Complex number
print(type('Brigette'))  # String
print(type([1, 2, 3]))   # List
print(type(['Brigette', 'Finland', 'Python']))   # List
print(type({'name':'Brigette'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#operators
a=4
b=5
c=a+b
print(c)

#comparison operators
print(4 > 3)
print(4 >= 3)
print(4 >= 4)
print(3 > 4)
print(5 == 5)
print('what is the value here', 5 != 5)
print(4 != '4')
print(4 == '4')
print(4 < 4)
print(4 is 4)
print(2 is not 4)
print(2 is not 2)
print('land' in 'Finland')
print('land' in 'Sweden')

#logical operators

print(4 > 3 and 2 < 3)
print(4 < 3 and 2 < 3)

print(4 > 3 or 2 < 3)
print(4 < 3 or 2 < 3)

print(not 4 > 3)
print(not not 4 > 3)