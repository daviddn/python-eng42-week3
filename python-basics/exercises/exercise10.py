# Story book!

# Create a dictionary with 3 stories inside! Like a book :)
# each story should be its own dictionary with:
    # beginning, middle, end
    # hero

# Iterate over the book, and print out each story! PRINT ALL of them :)
# Formatted of course

# hints:
    # you already built a dictionary with a story
    # you already have something to prompt user for input & build dictionaries
    # Now what we want is to create a book that hold 3 stories

# extra:
    # stick it in a while loop so we continue to listen to stories :)
    # it would be nice to be able to read only one story

book1_dict = {}
book2_dict = {}
book3_dict = {}

storybook_dict = {
    'book 1': book1_dict,
    'book 2': book2_dict,
    'book 3': book3_dict
}

book1_dict['hero'] = input('Who is the hero of your story? ').capitalize()
book1_dict['beg'] = input('Write out a sentence for the beginning of you story! ').capitalize()
book1_dict['mid'] = input('Write out a sentence for the middle of you story! ').capitalize()
book1_dict['end'] = input('Write out a sentence for the end of you story! ').capitalize()

book2_dict['hero'] = input('Who is the hero of your story? ').capitalize()
book2_dict['beg'] = input('Write out a sentence for the beginning of you story! ').capitalize()
book2_dict['mid'] = input('Write out a sentence for the middle of you story! ').capitalize()
book2_dict['end'] = input('Write out a sentence for the end of you story! ').capitalize()

book3_dict['hero'] = input('Who is the hero of your story? ').capitalize()
book3_dict['beg'] = input('Write out a sentence for the beginning of you story! ').capitalize()
book3_dict['mid'] = input('Write out a sentence for the middle of you story! ').capitalize()
book3_dict['end'] = input('Write out a sentence for the end of you story! ').capitalize()

# print(f"Great! So the mighty hero of your story is the legendary {book1_dict['hero']}! He is faced by his worst enemy, Buttercup, the most evil entity in the universe. The adventure takes place in the popular tourist location of Lisboa. {book1_dict['beg']}. {book1_dict['mid']}. {book1_dict['end']}. The end(?)")
#
# print(f"Great! So the mighty hero of your story is the legendary {book2_dict['hero']}! He is faced by his worst enemy, Buttercup, the most evil entity in the universe. The adventure takes place in the popular tourist location of Lisboa. {book2_dict['beg']}. {book2_dict['mid']}. {book2_dict['end']}. The end(?)")
#
# print(f"Great! So the mighty hero of your story is the legendary {book3_dict['hero']}! He is faced by his worst enemy, Buttercup, the most evil entity in the universe. The adventure takes place in the popular tourist location of Lisboa. {book3_dict['beg']}. {book3_dict['mid']}. {book3_dict['end']}. The end(?)")

start_input = ''

while start_input != 'exit':
    start_input = input('Please give a number between 1 and 3 to start reading a story, or write exit to leave: ').lower()
    if start_input == '1':
        print(f"Great! So the mighty hero of your story is the legendary {book1_dict['hero']}! He is faced by his worst enemy, Buttercup, the most evil entity in the universe. The adventure takes place in the popular tourist location of Lisboa. {book1_dict['beg']}. {book1_dict['mid']}. {book1_dict['end']}. The end(?)")
    elif start_input == '2':
        print(f"Great! So the mighty hero of your story is the legendary {book2_dict['hero']}! He is faced by his worst enemy, Buttercup, the most evil entity in the universe. The adventure takes place in the popular tourist location of Lisboa. {book2_dict['beg']}. {book2_dict['mid']}. {book2_dict['end']}. The end(?)")
    elif start_input == '3':
        print(f"Great! So the mighty hero of your story is the legendary {book3_dict['hero']}! He is faced by his worst enemy, Buttercup, the most evil entity in the universe. The adventure takes place in the popular tourist location of Lisboa. {book3_dict['beg']}. {book3_dict['mid']}. {book3_dict['end']}. The end(?)")
    else:
        print('Input not recognized.')