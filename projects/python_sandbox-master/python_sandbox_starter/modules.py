# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime                 # datetime = preinstalled python module
from datetime import date       # import only the date function/method from the datetime module
import time

# Pip module
# import camelcase
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email

today = datetime.date.today()
hoy = date.today()
timestamp = time.time()

c = CamelCase()
print(c.hump('hello there world'))

email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')

# print(today)
# print(hoy)
# print(timestamp)

# Install a Python package with pip/pip3; in this case the 'camelcase' package
# pip3 install camelcase        # run in terminal

# View all Python packages installed
# pip3 freeze                   # run in terminal

