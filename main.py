import json
from rich import print

class Validator():
    def __init__(self,validWords):
        self.green = {1:0,2:0,3:0,4:0,5:0}
        self.yellow = {1:0,2:0,3:0,4:0,5:0}
        self.grey = set()
        self.validWords = validWords
    
    # little bit of inefficiency since i am rechecking old greens everytime i do green validator but its kept for a repeated green letter that is now grey    
    def greenValidator(self):
        for position in self.green.keys():
            letter = self.green.get(position)
            if letter == 0:
                continue
            for word in list(self.validWords.keys()):
                if word[position - 1] != letter:
                    del self.validWords[word]
    
    def yellowValidator(self):
        for position in self.yellow.keys():
            letter = self.yellow.get(position)
            if letter == 0:
                continue
            for word in list(self.validWords.keys()):
                if letter not in word or word[position - 1] == letter:
                    del self.validWords[word]
        self.yellow = {1:0,2:0,3:0,4:0,5:0}
                        
    def greyValidator(self):
        checkGreen = []
        for letter in self.green.values():
            if letter != 0:
                checkGreen.append(letter)
        for letter in self.grey:
            if letter in checkGreen:
                for word in list(self.validWords.keys()):
                    if word.count('letter') > 1:
                        del self.validWords[word]
                continue
            for word in list(self.validWords.keys()):
                if letter in word:
                    del self.validWords[word]
                    continue
        self.grey = set()
    
    def finishedWord(self):
        state = False
        if 0 not in self.green.values():
            state = True
        return state
    
    def letterUpdater(self,greyLetters,yellowLetters,greenLetters):
        if greyLetters.lower() != '':
            for letter in greyLetters:
                self.grey.add(letter)
        if yellowLetters.lower() != '':
            temp_yellow = yellowLetters.split(',')
            for letter in temp_yellow:
                self.yellow[int(letter[0])] = letter[1]
        if greenLetters.lower() != '':
            temp_green = greenLetters.split(',')
            for letter in temp_green:
                self.green[int(letter[0])] = letter[1]
             
    def nextGuess(self):
        return self.validWords
    
if __name__ == '__main__':
    with open('words_dictionary.json', 'r') as file:    
        validWords = json.load(file)

    wordle = Validator(validWords)
    while wordle.finishedWord() == False:
        greyLetters = input('Grey Letters: ')
        yellowLetters = input('Yellow Letters (Comma separated): ')
        greenLetters = input('Green Letters (Comma separated): ')
        wordle.letterUpdater(greyLetters,yellowLetters,greenLetters)
        if greenLetters != '':
            wordle.greenValidator()
        if yellowLetters != '':
            wordle.yellowValidator()
        if greyLetters != '':
            wordle.greyValidator()
        print(wordle.nextGuess())
        print(len(wordle.nextGuess()))
