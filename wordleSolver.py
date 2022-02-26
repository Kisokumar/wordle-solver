import sys
wordsPath = sys.argv[1]

def wordleSolver(exclude,correctPosition):
    with open(wordsPath,'r') as possibleWords:
        possibleWords = possibleWords.read()
    
    
    possibleWords = list(possibleWords.split())
    exc = [c for c in exclude]

    for word in possibleWords:
        temp = [c for c in word]
        possible = True

        for i in exc:
            if i in word:
                possible = False
                break
        
        for i,j in enumerate(correctPosition):
            if j!='':
                if temp[i]!=j:
                    possible = False


        if possible:
            print(word)
     
wordleSolver('elo',['a','','n','',''])

# wordleSolver(incorrect letters,[correct letters])
# wordleSolver(grey letters,[list of green letters])

# input = 'elo',['a','','n','','']
# output = annul,aunty