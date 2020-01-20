import random

play = True

while play:
    print(f'\nI am thinking of a number between 1 and 100.')
    print('Can you guess what number I am thinking of in 5 guesses of less?')

    secret_number = random.randint(1, 100)
    guesses = 5
    user_num = 0
    play_again = ''

    while guesses > 0:
        print(f'\nGuesses remaining: {guesses}')
        guesses -= 1
        try:
            user_num = int(input(f'\nEnter your guess: '))
        except ValueError:
            print('I need a number!')
            guesses += 1
            continue
        if user_num == secret_number:
            break
        if user_num < secret_number:
            print('Too low!')
        if user_num > secret_number:
            print('Too high!')

    if user_num == secret_number:
        print(f'\nHooray for you!  You guessed it!')
    if user_num != secret_number:
        print('You are out of guesses.')

    while play_again not in {'y', 'n'}:
        play_again = input(f'\nWould you like to try again? (y)es or (n)o: ')
        play_again = play_again.lower()
        if play_again not in {'y', 'n'}:
            print(f'\nInvalid! y or n')
        elif play_again == 'n':
            print(f'\nHave a nice day!')
            play = False
