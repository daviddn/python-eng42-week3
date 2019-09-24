# Define the following variables
# name, last_name, age, eye_color, hair_color
name = 'David'
last_name = 'Naim'
age = 21
eye_color = 'Black'
hair_color = 'Black'

# Prompt user for input and Re-assign these
name = input('What is your name? ').capitalize()
last_name = input('What is your last name? ').capitalize()
age = int(input('How old are you? '))
eye_color = input('What is your eye color? ')
hair_color = input('What is your hair color? ')

print(f'Hello {name} {last_name}! Welcome, your age is {age}, your eyes are {eye_color.lower()} and your hair is {hair_color.lower()}')

birthdate = 2019-age

print(f'Also, since your age is {age}, then you must have been born in {birthdate}!')

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair is black'