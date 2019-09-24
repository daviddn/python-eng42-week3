# # Numerical Data types
# # - Int, long, float, complex
# # These are numerical data types which we can use numerical operators.
#
# # Complex and Long we don't use as much
# # Complex bring an imaginary type of number
# # long - are integers of unlimited size
#
# # int - Stands for integers
# # Whole numbers
# my_int = 10
# print(my_int)
# print(type(my_int))
#
# # Operator - Add, Subtract, Divide and Multiply
#     # Exponential
# print(4+3)
# print(4-3)
# print(4/2) # Division automatically converts to float
# print(4//2) # Keeps it as integer / drops the decimal
# print(4*2)
# print(3**2)
#
# # Modulus looks for the number of remainders
# # %
# print(5%2)
#
# # Comparison Operators # --> boolean value
#
# # == - Comparision Operator
# # < / > - Bigger and smaller than
# # <= - Smaller than or equal
# # >= - Bigger than or equal
# # != - Not equal
# # is and is not
#
# my_variable1 = 10
# my_variable2 = 13
#
# print(my_variable1 == my_variable2)
# print(my_variable1 > my_variable2)
# print(my_variable1 < my_variable2)
# print(my_variable2 >= 13)
# print(my_variable2 is 13)
# print(my_variable2 is not 13)
#
# # Boolean Values
# # Defined by either True or False
# print(type(True))
# print(type(False))
# print(0 == False)
# print(1 == True)
#
# ## None
# print(None)
# print(type(None))
# print(bool(None))

print('Logical *and* & *or* ------')
# Logical *and* & *or*
a = True
b = False
# Using *and* both sides have to be true for it to result in true
print(a and True)
print((1 == 1) and (True))
print((1 == 1) and False)

# Use or, ONLY 1 side needs to be true
print('this will print True')
print(True or False)
print(True or 1 == 2)
print('this will print False')
print(False or 1 == 2)