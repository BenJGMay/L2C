import random
guess = ''
guesses = 0

colours = ['red', 'blue', 'green', 'white', 'black', 'pink', 'yellow', 'orange']

colour = random.choice(colours)

while guess != colour:
    guess = input('What colour am I thinking of? ')
    guesses += 1

if guesses == 1:
    print('You got it! It took you', guesses, 'guess.')
else:
    print('You got it! It took you', guesses, 'guesses.')
