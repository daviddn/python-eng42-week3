# Nested listed and dicitonaries

# nested_list = ['bread', 'sugar', [1, 2, 3, 4, 'spice', {'name': 'Buttercup'}]]
#
# print(nested_list[2][5]['name'])
#

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'completed modules': ['sword', 'augmented senses', 'no face', 'no name']
}

students = {
    '1': student1,
    '2': {
    'name': 'Stirling Archer',
    'stream': 'Chaos',
    'grade': 10,
    'completed modules': ['danger', 'robust liver', 'mummy issues', 'espionage']
}
}

count = 1
for key in students:
    #print(f'{key}: {students[key]}')
    count = 1
    for name in students[key]:
        print(f'{count} - {name}: {students[key][name]}')
        count += 1

# print(students['1']['name'])
# print(students['2']['name'])

