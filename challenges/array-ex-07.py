# Unique characters in a string:
# given a string, determine if it is compreised of all unique characters. the string 'abcde' has all unique characters and should return true.

def unique_char(s):
    
    char = set()

    for letter in s:
        if letter in char:
            return False
        else:
            char.add(letter)

    return True