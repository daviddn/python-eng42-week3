# The game POP AND TOC!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are POPTOC

# As a user I should be asked for a number,
# so that I can play the game with my input

# As a player, I should see the game counting up to my number
# and substituting the multiples of 3 and 5 with the respective values,
# so that I can see if it is working

# As a player, I should be able to exit the game using a keyword,
# so that I can stop playing

player_input = ''

while player_input != 'exit':
    player_input = int(input('Welcome to POP AND TOC! A game for all ages! Input a number please: '))
    if player_input%3 == 0 and player_input%5 == 0:
        print('POPTOC')
    elif int(player_input)%3 == 0:
        print('POP')
    elif int(player_input)%5 == 0:
        print('TOC')
    else:
        'Not a valid number! Please try again: '