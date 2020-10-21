# Create your Phrase class logic here.
class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def display(self, guesses):
        for i in range(len(guesses)):
            for j in range(len(self.phrase)):
                if guesses[i] == self.phrase[j]:
                    print('{}'.format(guesses[i]), end=' ')
                else:
                    print('_', end=' ')
        print()

    def check_letter(self, guess):
        if guess in self.phrase:
            return True
        return False 

    def check_complete(self):
        pass
