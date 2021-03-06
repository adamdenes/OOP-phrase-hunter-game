# Create your Phrase class logic here.
class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print('{}'.format(letter), end =' ')
            else:
                print('_', end=' ')

    def check_letter(self, guess):
        if str(guess) in self.phrase:
            return True
        return False 

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
