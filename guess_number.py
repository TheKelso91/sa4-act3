number = 10

print("I'm thinking of a number...")

while True:
    max_guesses = 3
    current_guesses = 0
    
    guess = (input('What number am I thinking of? '))
    if guess == number:
        print('Congratulations! You guessed the right number.')
        break
    if guess == 'q':
        print(f"That's okay, the number was {number}.")
        break
    else:
        current_guesses += 1
        if max_guesses == current_guesses:
            print(f'Sorry! The number that is the wrong number. You have run out of guesses.')
        else:
            print(f'Sorry, that number is wrong. You have {max_guesses - current_guesses} left.')
