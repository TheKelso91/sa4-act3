number = 10

print("I'm thinking of a number...")

while True:
    guess = (input('What number am I thinking of? '))
    if guess == number:
        print('Congratulations! You guessed the right number.')
        break
    if guess == 'q':
        print(f"That's okay, the number was {number}.")
        break
    else:
        print(f'Sorry! The number that is the wrong number. Try again.')