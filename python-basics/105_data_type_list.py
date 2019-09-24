# List
# List keep object in order of index
# It's defined by []

# example of a list - index
# list-name     = [    0     ,   1   ,    2    ,    3   ]
crazy_x_partner = ['Carolina', 'JSON', 'Arthur', 'Lana!']

# print and show type (Read ALL)
print(crazy_x_partner)
print(type(crazy_x_partner))

# Get a particular record out (Read one)
# Lists are organized with index
print(crazy_x_partner[0]) # use the index inside square brackets [i]

# How do I print the last one?
print(crazy_x_partner[-1])

# Maybe we want to change a record in a specific index?
    # Reassign an index
print(crazy_x_partner[3])
crazy_x_partner[3] = 'LANAA!! (...) DANGER ZONE!!!'
print(crazy_x_partner[3])

# Add more people to the list (Create one) - append()
print(crazy_x_partner)
crazy_x_partner.append('Cyral Figus')
print(crazy_x_partner)

# Insert in index specific location
crazy_x_partner.insert(3, 'Malorie')
print(crazy_x_partner)
crazy_x_partner.insert(3, 'Malorie')
print(crazy_x_partner)

# Remove someone from the list (Destroy one)
crazy_x_partner.remove('JSON')
print(crazy_x_partner)
crazy_x_partner.remove('Malorie') # Removes based on object
print(crazy_x_partner)

# Remove using index
crazy_x_partner.pop() # Removes last index
print(crazy_x_partner)

crazy_x_partner.pop(1) # Removes based on index
print(crazy_x_partner)

# Mixed data and List
# Lists can have many data types
hybrid_list = ['this is a string', 12, 66, 'hello', [1,2,3], [1,2,2]]

# What happens when you have 3500000?
# Loops and other data formats

# Tuples --> Immutable lists
# They do not change
# Syntax
# my_tuple = ()
# tuples are defined by (), not using square brackets
my_tuple = (2, 'hello', 22, 'more value')
print(my_tuple)
print(type(my_tuple))

# Range slicing
print(crazy_x_partner)
print(crazy_x_partner[:1]) # 0 to 1, not inclusive of 1
print(crazy_x_partner[1:2]) # from 1 to 2, not inclusive of 2

# Jumping/slicing
# syntax [N::M]
# N is where it starts
# M is every record it prints
example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(example_list[::3])
print(example_list[1::3])