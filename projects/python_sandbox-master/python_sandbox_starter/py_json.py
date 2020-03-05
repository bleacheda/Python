# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON (create a JSON dictionary - uses double quotes)
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# Create a Python dictionary
car = {'make': 'ford', 'model': 'mustang', 'year': 1970}

# Parse it to JSON
carJSON = json.dumps(car)

print(carJSON)
