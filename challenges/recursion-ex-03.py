# Reverse a string using recursion.

def reverse_string(word, result = ''):
    try:
        result += word[len(word)-1]

        return reverse_string(word[0:len(word)-1], result)

    except IndexError:

        return result



print(reverse_string('GIRAFARIJ'))

