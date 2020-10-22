# Create your Game class logic in here.
import re
import sys
import random
from phrasehunter.phrase import Phrase


class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase('What Goes Up Must Come Down'),
            Phrase('Hard Pill to Swallow'),
            Phrase('Right Off the Bat'),
            Phrase('Down And Out'),
            Phrase('Man of Few Words')
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']

    def start(self):
        self.welcome()

        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print('Number missed: {}\n'.format(self.missed))
            self.active_phrase.display(self.guesses)
            print()

            user_guess = self.get_guess()
            self.guesses.append(user_guess)

            if not self.active_phrase.check_letter(user_guess):
                self.missed += 1

        self.game_over()

    def get_random_phrase(self):
        rand_numb = random.randint(0, len(self.phrases)-1)
        return self.phrases[rand_numb]

    def welcome(self):
        welcome = 'Welcome to Phrase Hunter!'
        empty = ' ' * len(welcome)
        print('#############################')
        print('# {} #'.format(empty))
        print('# {} #'.format(welcome))
        print('# {} #'.format(empty))
        print('#############################')
        print()

    def get_guess(self):
        while True:
            try:
                guess = input('\nGuess a letter: ').lower()

                if len(guess) != 1:
                    raise ValueError(
                        '\nOnly one character should be used at a time!')
                elif re.match(r'\d+', guess, re.I):
                    raise ValueError('\nNumbers are not allowed!')
                elif re.match(r'[^\w]', guess, re.I):
                    raise ValueError(
                        '\nPlease only use letter characters! [a-z]')
                elif guess in self.guesses:
                    raise ValueError(
                        '\n"{}" was already guessed before!'.format(guess))
                else:
                    return guess
            except ValueError as ve:
                print('{} Please guess again...'.format(ve))
                continue
            except KeyboardInterrupt:
                print('\nTerminated by player! Exiting...')
                sys.exit()

    def game_over(self):
        if self.missed == 5:
            print('\nGame Over! Better luck next time...')
        else:
            print('\nCongratulations! You Won!')

        while True:
            try:
                new_game = input('Do you want to play again? [y/n] ').upper()

                if new_game == 'Y':
                    ngame = Game()
                    ngame.start()
                elif new_game == 'N':
                    print('See you around!')
                    sys.exit()
                else:
                    raise ValueError('Y or N expected!')
            except ValueError as ve:
                print('{} You have typed "{}"...'.format(ve, new_game))
                continue
            except KeyboardInterrupt:
                print('\nTerminated by player! Exiting...')
                sys.exit()
