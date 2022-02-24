import sys

wordsPath = sys.argv[1]

with open(wordsPath,'r') as possibleWords:
    possibleWords = possibleWords.read()


print(possibleWords)




