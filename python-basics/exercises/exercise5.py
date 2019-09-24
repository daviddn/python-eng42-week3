# Assignment for post class
# Use variables, print and different data types
# Ask and store the following in variables:
    # Name, last_name, age, age of mother, 3 skills

    # Print out the information in a formatted manner
    # Calculate age difference between response and mother
    # Store skills in a list
    # Print each skill in a formatted way

# Definition of formatted
    # a little context text
    # appropriate string formatting like lower case or upper case or other

first_name = input("Hello, what's your name? ").capitalize()
last_name = input('Now what about your last name? ').capitalize()
age = int(input('How old are you? '))
age_of_mother = int(input('How old is your mother? '))
skill_1 = input('Can you tell me a skill of yours? ').lower()
skill_2 = input('Can you tell me another skill of yours? ').lower()
skill_3 = input('Can you tell me another skill of yours one last time? ').lower()

age_diff = (age_of_mother-age)
skills_list = [skill_1, skill_2, skill_3]

print(f'Thank you for answering {first_name} {last_name}! You are {age} years old, while your mother is {age_of_mother} years old! You and your mother have an age difference of {age_diff} years! Wow!')

print(f'Also, you have an impressive set of skills! {skills_list[0].capitalize()}, {skills_list[1]}, and {skills_list[2]}. Just look at them! I bet you like {skill_1} more than {skill_2}, and I do not really believe that you know {skill_3}!')