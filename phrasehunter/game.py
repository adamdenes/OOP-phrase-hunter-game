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

        while self.missed <= 5:
            print('Number missed: {}'.format(self.missed))
            print()
            self.active_phrase.display(self.guesses)
            print()

            user_guess = self.get_guess()
            self.guesses.append(user_guess)

            if not self.active_phrase.check_letter(user_guess):
                self.missed += 1

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
        guess = input('Guess a letter: ')
        return guess

    def game_over(self):
        pass
