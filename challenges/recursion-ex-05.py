# STRING PERMUTATION

# given a string 'abc', write a function that returns all possible combination of 'a' 'b' and 'c' in a list.
import itertools

def permute(word):

    out = []
    # base case
    if len(word) == 1:
        out = [word]

    else:
        # for every letter in string:

        for i, let in enumerate(word):

            #for every permute:

            for perm in permute( word[:i] + word[i+1:]):
                print('current letter is:', let)
                print('current perm is:', perm)
                # Add it to output
                out += [let + perm]

    return out



print(permute('123'))


