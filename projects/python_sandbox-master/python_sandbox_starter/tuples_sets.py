# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor to create a tuple
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
# print(fruits, fruits2)

# Single value tuple needs trailing comma
fruits2 = ('Apples',)

# Get tuple value; zero based
print(fruits[1])

# Can't change value, the below will give an error
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangos'}

# Check if a certain value is in a set; output is True/False
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Add duplicate; will not give an error but it won't actually add the duplicate value to the set
fruits_set.add('Apples')

# Clear set; clears the contents of the set without deleting the set
# fruits_set.clear()

# Delete a set; completely deletes the set (and its contents obviously)
# del fruits_set

# Print set; will print the elements of the set in a different order everytime you run it

print(fruits_set)