import json
from rich import print

class Validator():
    def __init__(self,validWords):
        self.green = {1:0,2:0,3:0,4:0,5:0}
        self.yellow = {1:0,2:0,3:0,4:0,5:0}
        self.grey = set()
        self.validWordsSize = len(validWords)
        self.removedWordsSize = 0
        self.validWords = validWords
    
    # little bit of inefficiency since i am rechecking old greens everytime i do green validator but its kept for a repeated green letter that is now grey    
    def greenValidator(self):
        for position in self.green.keys():
            letter = self.green.get(position)
            if letter == 0:
                continue
            i = 0
            while i < (self.validWordsSize - self.removedWordsSize):
                word = self.validWords[i]
                if word[position - 1] != letter:
                    self.validWords.remove(word)
                    self.removedWordsSize += 1
                else:
                    i += 1
    
    def yellowValidator(self):
        for position in self.yellow.keys():
            letter = self.yellow.get(position)
            if letter == 0:
                continue
            i = 0
            while i < (self.validWordsSize - self.removedWordsSize):
                word = self.validWords[i]
                if letter not in word or word[position - 1] == letter:
                    self.validWords.remove(word)
                    self.removedWordsSize += 1
                    i -= 1
                else:
                    i += 1
        self.yellow = {1:0,2:0,3:0,4:0,5:0}
                        
    def greyValidator(self):
        checkGreen = []
        for letter in self.green.values():
            if letter != 0:
                checkGreen.append(letter)
        for letter in self.grey:
            if letter in checkGreen:
                for word in self.validWords:
                    if word.count('letter') > 1:
                        self.validWords.remove(word)
                continue
            i = 0
            while i < (self.validWordsSize - self.removedWordsSize):
                word = self.validWords[i]
                if letter in word:
                    self.validWords.remove(word)
                    self.removedWordsSize += 1
                    continue
                i += 1
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
    wordList = []
    for word in validWords:
        wordList.append(word)
    
    wordle = Validator(wordList)
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
