import json
from rich import print

with open('words_dictionary.json', 'r') as file:    
    validWords = json.load(file)

frequencyLetters = {}
frequencyLettersPosition = {1:{},2:{},3:{},4:{},5:{}}
for word in validWords:
    try:
        frequencyLettersPosition[1][word[0]] += 1
    except KeyError:
        frequencyLettersPosition[1].setdefault(word[0], 1)
    try:
        frequencyLettersPosition[2][word[1]] += 1
    except KeyError:
        frequencyLettersPosition[2].setdefault(word[1], 1)
    try:
        frequencyLettersPosition[3][word[2]] += 1
    except KeyError:
        frequencyLettersPosition[3].setdefault(word[2], 1)
    try:
        frequencyLettersPosition[4][word[3]] += 1
    except KeyError:
        frequencyLettersPosition[4].setdefault(word[3], 1)
    try:
        frequencyLettersPosition[5][word[4]] += 1
    except KeyError:
        frequencyLettersPosition[5].setdefault(word[4], 1)
    for letter in word:
        try:
            frequencyLetters[letter] += 1
        except KeyError:
            frequencyLetters.setdefault(letter, 1)

frequencyLetters = (sorted(frequencyLetters.items(), key=lambda x:x[1], reverse=True))
vowels = ['a','e','i','o','u']
for word in validWords:
    validWords[word] = 0
    countVowels = sum(1 for vowel in vowels if vowel in word)
    for i in range(1,6):
        frequencyLettersPositioni = (sorted(frequencyLettersPosition[i].items(), key=lambda x:x[1], reverse=True))
        if frequencyLettersPositioni[0][0] in word:
            validWords[word] += 15
        if frequencyLettersPositioni[1][0] in word:
            validWords[word] += 12
        if frequencyLettersPositioni[2][0] in word:
            validWords[word] += 9
        if frequencyLettersPositioni[3][0] in word:
            validWords[word] += 6
        if frequencyLettersPositioni[4][0] in word:
            validWords[word] += 3
    if frequencyLetters[0][0] in word:
        validWords[word] += 15
    if frequencyLetters[1][0] in word:
        validWords[word] += 12
    if frequencyLetters[2][0] in word:
        validWords[word] += 9
    if frequencyLetters[3][0] in word:
        validWords[word] += 6
    if frequencyLetters[4][0] in word:
        validWords[word] += 3
    if frequencyLetters[-1][0] in word:
        validWords[word] -= 15
    if frequencyLetters[-2][0] in word:
        validWords[word] -= 12
    if frequencyLetters[-3][0] in word:
        validWords[word] -= 9
    if frequencyLetters[-4][0] in word:
        validWords[word] -= 6
    if frequencyLetters[-5][0] in word:
        validWords[word] -= 3
    if countVowels >= 3:
        validWords[word] += 10
    if countVowels == 2:
        validWords[word] += 7
    if countVowels == 1:
        validWords[word] += 5
    if countVowels == 0:
        validWords[word] -= 5
    repeatedLetters = []
    for character in set(word):
        if word.count(character) > 1:
            repeatedLetters.append(character)
    if len(repeatedLetters) >= 1:
        validWords[word] -= 5 * len(repeatedLetters)
        
validWords = dict(sorted(validWords.items(), key=lambda x:x[1], reverse=True))

with open('words_dictionary.json', 'w') as file:    
    json.dump(validWords,file,indent = 4)
