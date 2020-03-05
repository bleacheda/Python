# A List is a collection which is ordered and changeable. Allows duplicate members. Lists are zero based (0 = first index/position in a list)

# Create a list
numbers = [1, 2, 3, 4, 5]                           # list of int
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']   # list (array) of strings

# Use a constructor; not really used?
# numbers2 = list((1,2,3,4,5))

# print(numbers,numbers2)
# print(numbers, fruits)
# print(fruits)

# Get a value; lists are zero based
print(fruits[1])

# Get length of list
print(len(fruits))

# Get length of list item at position x
print(len(fruits[0]))

# Append to list
fruits.append('Mangos')

# Remove from list by specifiying the value to be removed
fruits.remove('Grapes')

# Insert into position; insert(index, value)
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop = remove from list by specifying the index
fruits.pop(2)

# Reverse the list
fruits.reverse()

# Sort the list in alphabetical order
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)