import time
# While loops!

# Keeps looping and iterating until a condition is met
# Or it comes into a BREAK statement

# Syntax 1
# while <condition>:
    # Block

# Syntax 2
# while <condition>:
    # Block
    # if <condition>:
        # Break

# counter = 0
# while counter < 10:
# #     print(counter)
# #     print('PEWWWWDIEEEPIEEEE')
# #     counter += 1
# #     time.sleep(1)

# while True:
#     print('WAAAHHHH')
#     print(counter)
#     if counter >= 10:
#         break
#     counter += 1

# if input is 'exit' i want to exit
# if input is 'cute' --> Awww Jigglypuff ... <3
# ELSE I want to shout back JIGGGGGLYYYYYPUFFFFF!!!!

# user_input = ''
#
# while user_input != 'exit':
#     print("What's up Jigglypuff")
#     user_input = input()
#     if user_input == 'cute':
#         print("Awww Jigglypuff ... <3")
#     else:
#         print('JIGGGGGLYPUFFFFF!!!!')
#         print('JIGGGGGLYYPUFFFFFFFF')

cars = ['volvo', 'skoda', 'ferrari', 'Lambo']

counter = 0
max_length = len(cars)
while counter < max_length:
    print(cars[counter])
    counter += 1
