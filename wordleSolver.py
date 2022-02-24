import sys
wordsPath = sys.argv[1]

def wordleSolver(exclude):
    with open(wordsPath,'r') as possibleWords:
        possibleWords = possibleWords.read()
    
    possible = True
    possibleWords = list(possibleWords.split())
    exc = [c for c in exclude]

    for word in possibleWords:

        for i in exc:
            if i not in word:
                possible = False
        
        if possible:
            print(word)
     
wordleSolver('abc')

# input = abc
# output = aback