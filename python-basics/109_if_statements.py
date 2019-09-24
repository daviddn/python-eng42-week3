# Control Flow - If statements
# Controls where the code is going to go.
# Depending on the result of the evaluations that return True or False, it runs a block of code or not.

# syntax
# if <condition>:
    # block
# elif <condition>:
    # block
    # do stuff
# else:
    # block

weather = 'snowy and rainy and stormy'

if ('rainy' in weather) and ('stormy' in weather):
    print('stay home')
elif 'rainy' in weather:
    print('take an umbrella')
elif 'snowy' in weather:
    print('wear boots and scarf')
else:
    print('take shades')

age = 16
driver_license = False

# - You can vote and drive
# - You can vote
# - You can drive
# - You can't legally drink but your mates/uncles might have your back (bigger 16)
# - You're too young, go back to school!

if (age >= 18) and (driver_license == True):
    print('You can vote and drive!')
elif (age > 18) and (driver_license == False):
    print('You can vote!')
elif (age < 18) and (driver_license == True):
    print('You can drive!')
elif 16<=age<18:
    print("You can't legally drink but your mates/uncles might have your back!")
else:
    print("You're too young, go back to school!")