valid_words = []

with open('wordle_dictionary.txt', 'r') as file:
  words = file.readlines()
  for word in words:
    valid_words.append(word.strip())

def finished_word(green):
  state = False
  if len(green) == 5:
    state = True
  return state

def green_validator(green, valid_words, validWordsSize, removedWordsSize):
  for position in green.keys():
      letter = green.get(position)
      i = 0
      while i != (validWordsSize - removedWordsSize):
          word = valid_words[i]
          if word[position - 1] != letter:
              valid_words.remove(word)
              removedWordsSize += 1
              i = 0
          else:
              i += 1
  return valid_words, validWordsSize, removedWordsSize

def yellow_validator(yellow, valid_words, validWordsSize, removedWordsSize):
  for letter in yellow.keys():
      position = yellow.get(letter)
      i = 0
      while i != (validWordsSize - removedWordsSize):
          word = valid_words[i]
          if letter not in word or word[position - 1] == letter:
              valid_words.remove(word)
              removedWordsSize += 1
              i = 0
          else:
              i += 1
  return valid_words, validWordsSize, removedWordsSize

def grey_validator(grey, green, valid_words, validWordsSize, removedWordsSize):
  checkGreen = []
  for letter in green.values():
    checkGreen.append(letter)
  for letter in grey:
    if letter in checkGreen:
      for word in valid_words:
        if word.count('letter') > 1:
          valid_words.remove(word)
      continue
    i = 0
    while i != (validWordsSize - removedWordsSize):
        word = valid_words[i]
        if letter in word:
            valid_words.remove(word)
            removedWordsSize += 1
            i = 0
        else:
            i += 1 
  return valid_words, validWordsSize, removedWordsSize

def main(valid_words):
  validWordsSize = len(valid_words)
  removedWordsSize = 0
  grey = set()
  yellow = dict()
  green = dict()
  while finished_word(green) == False:
    greys = input('Grey Letters: ')
    for letter in greys:
      grey.add(letter)
    yellows = input('Yellow Letters (Comma separated): ')
    if yellows.lower() != '':
      temp_yellow = yellows.split(',')
      for letter in temp_yellow:
        yellow.update({letter[1]:int(letter[0])})
    greens = input('Green Letters (Comma separated): ')
    if greens.lower() != '':
      temp_green = greens.split(',')
      for letter in temp_green:
        green.update({int(letter[0]):letter[1]})
    if greens != '':
      valid_words, validWordsSize, removedWordsSize = green_validator(green, valid_words, validWordsSize, removedWordsSize)
    if yellows != '':
      valid_words, validWordsSize, removedWordsSize = yellow_validator(yellow, valid_words, validWordsSize, removedWordsSize)
    if greys != '':
      valid_words, validWordsSize, removedWordsSize = grey_validator(grey, green, valid_words, validWordsSize, removedWordsSize)
    print(valid_words)

if __name__ == '__main__':
    main(valid_words)