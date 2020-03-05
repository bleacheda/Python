# Python has functions for creating, reading, updating, and deleting files.

# Open a file. Creates the file
myFile = open('myfile.txt', 'w')            # 'w' means write

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)         # doesn't close the file, just checks if it is closed or not
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and Ansible')
myFile.close()
# print('Is Closed: ', myFile.closed)

# Append to file
myFile = open('myfile.txt', 'a')        # 'a' means append; if you would use 'w' again it would overwrite the contents of the file
myFile.write(' and nothing else')
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')       # 'r+' means read
text = myFile.read(100)                 # read(100) means read 100 characters from file
print(text)
myFile.close()