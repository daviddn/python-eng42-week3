# String
# These are a list of characters put together
# Defined by '' or ""

# my_string = 'Amazing Grilled Fish'
# print(type(my_string))
# # You can print it
# print(my_string)

# Joining of Strings - Concatenation
first_name = 'Boris'
last_name = 'Becker'
print(first_name[0]) # string IS a list of characters. Therefore behaves like a list

# Concatenating 3 strings
full_name = first_name + ' ' + last_name
print(full_name)
print('string', 14)

# Interpolation
name = 'Rachel'
welcome_message = 'hey there, how youuu doin? ;)'
print(f'hey there, {name} how youuu doin? ;)')
# Place an f on the left/beginning of the string
# Then you can use {} to interpolate python variables inside


# Useful Methods for strings
my_string = '  Hello this is an amazing string    '

# count()
print(my_string.count('i'))
print(my_string.count(' '))

# .strip()
print(my_string.strip())

# len() # Not a method - general method bult in
print(len(my_string))

# .lower()
print(my_string.lower())

# .upper()
print(my_string.upper())

# .capitalized()
print(my_string.strip().capitalize())

# .replace(arg_int, arg_two)
print(my_string.replace('an', 'THE'))

# .split(arg) --> list
print(my_string.split(' '))
print(type(my_string.split(' ')))