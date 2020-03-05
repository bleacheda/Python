# A variable is a container for a value, which can be of various types

# Look up Python docstings and how to call them with __doc__

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x = 1             # int
y = 2.5           # float
name = 'John'     # str
is_cool = True    # bool    starts with capital letter e.g. True/False

# Multiple assignment
e, f, nombre, esta_cool = (10, 6.9, 'Ben', False)

# Basic Math
a = x + y

print('Hello')
print(x, y, name, is_cool)
print(e, f, nombre, esta_cool)
print(a)

# Print before casting
print(type(x), x, type(y), y)

# Casting
x = str(x)
y = int(y)
z = float(y)

# Print after casting
print(type(x), x, type(y), y)
print(type(z),z)


