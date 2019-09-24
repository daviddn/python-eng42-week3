# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg, General viewing, but some scenes may be unsuitable for young children
  ## 12, Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15, No one younger than 15 may see a 15 film in a cinema.
  ## 18, No one younger than 18 may see an 18 film in a cinema.

film_rating = input("What's the movie rating? ")

if film_rating.strip() == '18':
    print('No one younger than 18 may see this movie!')
elif film_rating.strip() == '15':
    print('No one younger than 15 may see this movie!')
elif film_rating.strip() == '12' or film_rating.upper().strip() == '12A':
    print('Not suitable for children aged under 12, unless accompanied by an adult!')
elif film_rating.lower().strip() == 'pg':
    print('General viewing, but some scenes may be unsuitable for young children!')
elif film_rating.lower().strip() == 'universal':
    print('Everyone can watch!')
else:
    print('Not a recognized film rating')
