import random

def main():
    number = random.randint(1, 9)
    guess = None
    
    while guess != number:
        guess = int(input('Guess a number between 1 and 9: '))
        if guess == number:
            print('Well guessed!')
main()
