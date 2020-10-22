# Create your Game class logic in here.
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
        guess = input('\nGuess a letter: ')
        return guess

    def game_over(self):
        if self.missed == 5:
            print('\nGame Over! Better luck next time...')
        else:
            print('\nCongratulations! You Won!')
