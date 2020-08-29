
##########################################################
#Using words.txt file

#open the file for reading.
fin = open('words.txt', 'r')
words = fin.readlines()
######optoinal itteration interface for the user########
##for k,v in anagrams.items():
##    print(k, v)
##    ask = input('continue (0/1):')
##    if not ask:
##        break


def normalizer(wordList):
    '''
    Strips new lines from words in a list and converts them to lowercase
    '''
    normWords = []
    for word in wordList:
        word = word.strip()
        word = word.lower()
        normWords.append(word)
    return normWords

def removeSingles(anagramsDict):
    '''
    Removes single element lists from a dicitonary of lists
    '''
    singletons = []
    for key,value in anagramsDict.items():
        if len(value) < 2:
            singletons.append(key)
    for key in singletons:
        del anagramsDict[key]
    return anagramsDict

def anagramFinder(wordList):
    '''
    Creates a dictionary for use in identifying anagrams in a word list
    '''
    #call the normalization function on the word list passed in
    normalizedWords = normalizer(wordList)
    anagrams = {}
    for word in normalizedWords:
        #turn the word into a list of letters and sort it
        orderedWord = sorted(list(word))
        #turn that back into a string to use as the key in the dictionary
        orderedWord = ''.join(orderedWord)
        #see if we have seen this pattern before
        if orderedWord in anagrams.keys():
            #if it is already in the dicitonary then append it to the list
            anagrams[orderedWord].append(word)
        else:
            #not in the dictionary so add it as a single item list
            anagrams[orderedWord] = [word]
    #Return the dicitonary of anagrams with single items removed
    return removeSingles(anagrams)


anagrams = anagramFinder(words)
