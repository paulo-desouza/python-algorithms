# Reverse the order of the words in the given string:
# my solution:
from re import I


def reverse(str):
    words = str.strip().split(' ')
    words.reverse()
    sentence = (' ').join(words)
    print(sentence)


# lecture solutions:
def reverse2(s):
    return " ".join(reversed(s.split()))

# best, saught solution:
def reverse3(s):

    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        
        if s[i] not in space:  #finds the first non-space
            word_start = i      #saves the index

            while i < length and s[i] not in space: #then, finds the first space after that

                i += 1

            words.append(s[word_start:i]) #and that's your word

        i += 1
        
    print(" ".join(reversed(words)))
        



reverse3('    This is the best')