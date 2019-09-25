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


while player_input != -1:
    counter = 0
    player_input = int(input('Welcome to POP AND TOC! A game for all ages! Input a number please, or -1 to exit: '))
    while counter < player_input:
        counter += 1
        if counter%3 == 0 and counter%5 == 0:
            print('POPTOC')
        elif int(counter)%3 == 0:
            print('POP')
        elif int(counter)%5 == 0:
            print('TOC')
        else:
            print(counter)
else:
    print('Bye!')