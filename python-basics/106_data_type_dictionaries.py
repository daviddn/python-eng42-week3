# # Dictionaries
# # All fun and games keep our crazy x list... but we also need more info
# # Introducing dictionaries!
#
# # Dictionaries are defined using {}
# # They are organized with keys that point to values
# # Much like looking up something on a dictionary or information about a contact on our phones
# # Thus in our phone, the contact Filipe Paiva will hold lot's of info for this entry
# # Could be the phone number, work number, email, address and so on...
#
# # Syntax
# # dict_name = {'example_key': 'value', 'example_key': 'value'}
#
# # Defining a simple dictionary with to keys
# dictionary_crazy_x = {
#     'Carolina': 'she was actually nice',
#     'Arthur': 'bit of a drinker'
# }
#
# print(dictionary_crazy_x)
# print(type(dictionary_crazy_x))
#
# # Accessing values - use the key!
# print(dictionary_crazy_x['Carolina'])
# print(dictionary_crazy_x['Arthur'])
#
# # Adding a new key, pair value
# dictionary_crazy_x['Kyle'] = 'Likes Monster'
# print(dictionary_crazy_x)
#
# dictionary_crazy_x['Kyle'] = 'REALLY Likes Monster'
# print(dictionary_crazy_x)
#
# # Get out all of the keys
# print(dictionary_crazy_x.keys())
#
# # Get out all of the values
# print(dictionary_crazy_x.values())
#
# # Remove item from dictionary
# dictionary_crazy_x.pop('Kyle')
# print(dictionary_crazy_x)

# Better example of a dictionary

crazy1 = {
    'name': 'Carolina',
    'phone': '07842715517',
    'address': 'Location 1, at places',
    'known places to avoid': ['Milan', 'Lisbon', 'Tavira']
}