# Variables in Python
 # Variable is a box. You can give it name a put stuff inside

# Assigning a Variable
# Giving box a name and putting sutff inside
box_variable = 'Books and stuff'

# Looking inside the box
print(box_variable)

# Re Assigning a Variable
# Variables are mutable - Hence they can change/be re-assigned
box_variable = "CD's and other stuff"
print(box_variable)

# Re Assigning with a integer
# Variable can hold any data type inside
box_variable = 14
print(box_variable)

# Important python function
# print(arg)
print('hello') # Printing string
print(box_variable) # Printing variable
print('hello', box_variable) # Overloading with two arguments

# type(arg)
# Output the data type of an object
print(type('hello'))
print(type(14))
print(type(14.0))
my_list = [1,2,2,'hey']
print(type(my_list))

variable_num = '14'
# print(type('10'*variable_num)) #This will break

# input()
# it prompts user for input
print('What is your favourite color?')
user_response = input('Now really, what is your favourite color? ')
print(user_response)