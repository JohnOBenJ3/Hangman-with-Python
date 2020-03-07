import random
import os


from words import words_list


def header():
    print('\n' + '=' * 50 + '\n')
    print(' ' * 22 + "HANGMAN" + ' ' * 22 + '\n')
    print('=' * 50 + '\n')


def clear():
    os.system("clear")


def start_game():
    clear()
    allowed_guesses = 6
    total_guesses = 0
    guess_list = []
    word = list(random.choice(words_list))
    blanks = "_" * len(word)
    blanks = list(blanks)

    header()
    print(blanks, '\n')

    while total_guesses < allowed_guesses:
        print(f'You have {allowed_guesses} guesses remaining.' + '\n')
        guess = input("Guess a letter...  ")
        for i, j in enumerate(word):
            if j == guess:
                blanks[i] = guess
                print(f'Nice! {guess} is in the word' + '\n')
                clear()
                header()

            elif j != guess:
                blanks[i] = blanks[i]
                clear()
                header()

        print('\n', blanks, '\n')
        guess_list.append(guess)
        print("PREVIOUS GUESSES", guess_list, '\n')

        if guess not in word:
            allowed_guesses -= 1

        if total_guesses == allowed_guesses:
            print(f'Sorry. The word was {"".join(word).upper()}' + '\n')
            play_again = input("Would you like to play again? Y/n  ")
            if play_again != 'n':
                start_game()
            break

        if "_" not in blanks:
            print(f'YOU WIN! the word was {"".join(word).upper()}' + '\n')
            play_again = input("Would you like to play again? Y/n  ")
            if play_again != 'n':
                start_game()
            break


start_game()
