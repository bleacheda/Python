# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Create a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person,type(person))

# Create a dictionary using a constructor
# person2 = dict(first_name='Sarah', last_name='Williams', age=40)
# print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dictionary keys
print(person.keys())

# Get dictionary items
print(person.items())

# Copy a dictionary
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove dictionary item
del(person2['age'])
person2.pop('phone')

# Clear
person2.clear()

print(person2)

# Get length
print(len(person))

# List of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
print(people[1]['name'])
print(people[1]['age'])