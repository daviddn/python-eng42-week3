# Assignment2 for post class

# Define an empty dictionary # name_dict = []

# Prompt user for input for a story
# It should have:
    # hero, beginning, middle, end.
    # 2 other things you define to be part of the story
    # add each response to the dictionary under an appropriate key

# Print out the dictionary information in an ordered way so we can read the story

story_dict = {}

story_dict['hero'] = input('Who is the hero of your story? ').capitalize()
story_dict['villain'] = input('Who is the villain of your story? ').capitalize()
story_dict['location'] = input('Where does the story take place? ').capitalize()
story_dict['beg'] = input('Write out a sentence for the beginning of you story! ').capitalize()
story_dict['mid'] = input('Write out a sentence for the middle of you story! ').capitalize()
story_dict['end'] = input('Write out a sentence for the end of you story! ').capitalize()

print(f"Great! So the mighty hero of your story is the legendary {story_dict['hero']}! He is faced by his worst enemy, {story_dict['villain']}, the most evil entity in the universe. The adventure takes place in the popular tourist location of {story_dict['location']}. {story_dict['beg']}. {story_dict['mid']}. {story_dict['end']}. The end(?)")