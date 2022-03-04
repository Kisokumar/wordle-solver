import sys
wordsPath = sys.argv[1]

def wordleSolver(exclude,correctPosition,wrongPosition,myLexicon):
    results = []
    exc =[c for c in exclude]
 
    with open(myLexicon,'r') as possibleWords:
        possibleWords = possibleWords.read()
        possibleWords = list(possibleWords.split())

    for word in possibleWords:
        temp = [c for c in word]
        correctWord = True
        for i in exc:
            if i not in correctPosition and i not in wrongPosition:
                if i in word:
                    correctWord = False

        for i,j in enumerate(correctPosition):
            if j!='':
                if temp[i]!=j:
                    correctWord = False

        for i,j in enumerate(wrongPosition):
            if j!='':
                for z in j:
                    if z not in temp:
                        correctWord = False
                    if temp[i]==z:
                        correctWord = False
        
        if correctWord:
            results.append(word)
    
    print('Number of possible words: ',len(results))
    print(results)

exc,correctPosition,wrongPosition='elo',['a','','n','',''],['','','','','']
wordleSolver(exc,correctPosition,wrongPosition,wordsPath)
# wordleSolver(incorrect letters,[correct position],[incorrect position], /path/to/words)
# wordleSolver(grey letters,[list of green letters],[list of yellow letters], /path/to/words)

# input = 'eo',['a','','n','',''],['','','','','']
# output = aunty