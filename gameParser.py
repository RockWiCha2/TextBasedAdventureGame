import string

skipWords = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def remove_punct(text):
    newText = ""
    for char in text:
        if not char in string.punctuation:
            newText = newText+char
    return newText

def remove_spaces(text):
    newtext = text.strip()
    return newtext

def remove_words(userInput, skip_words):
    wordsArray = userInput.split()
    newWords = []
    for i in wordsArray:
        if not i in skip_words:
            newWords.append(i)
            
            
    return newWords

def normalise_input(userInput):
    
    removedPunc = remove_punct(userInput)
    removedSpace = remove_spaces(removedPunc)
    removedWords = remove_words(removedSpace.lower(), skipWords)
    return removedWords
