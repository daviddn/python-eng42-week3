# syntax

# for <placeholder> in <iteratable>: # don't forget the colon
    # block of code
    # Indented gets run every iteration

cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Mustang Ford', 'Corvette']

# for car in cars:
#     print('hey :D ')
#     print(car)

# embedded_list = [['filipe', 'Francis'], ['Mustafa', 'David', 'Jillian']]
# #
# # for data in embedded_list:
# #     print(data)
# #     for name in data:
# #         print(name.capitalize())

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'completed modules': ['sword', 'augmented senses', 'no face', 'no name']
}

count = 1
for key in student1:
    print(f'{count} - {key}: {student1[key]}')
    count += 1