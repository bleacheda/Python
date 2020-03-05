# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Andrei'         # str
age = 38                # int   | to insert it into a string you need to cast it to type str first

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Positional Arguments
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in Python 3.6+)
print(f'Hello again, my name is {name} and I am {age}')


# String Methods
s = 'helloworld'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'   # sub = substring, count how many times substring 'sub' appears in string 's'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))    # result is True or False

# Ends with
print(s.endswith('d'))          # Result is True or False

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())