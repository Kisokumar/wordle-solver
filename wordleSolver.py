import sys
wordsPath = sys.argv[1]

def wordleSolver(exclude):
    with open(wordsPath,'r') as possibleWords:
        possibleWords = possibleWords.read()
    
    
    possibleWords = list(possibleWords.split())
    exc = [c for c in exclude]

    for word in possibleWords:
        possible = True

        for i in exc:
            if i in word:
                possible = False
        
        if possible:
            print(word)
     
wordleSolver('acdefjklnqrstuvwy')

# input = acdefjklnqrstuvwy
# output = hippo