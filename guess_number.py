number = 10

print("I'm thinking of a number...")

while True:
    guess = (input('What number am I thinking of? '))
    if guess == 'q':
        print(f"That's okay, the number was {number}.")
        break
    guess = int(guess)
    if guess == number:
        print('Congratulations! You guessed the right number.')
        break
    elif guess < number:
        print('Sorry, that guess was too low. Try again.')
    else:
        print('Sorry, that guess was too high. Try again.')
