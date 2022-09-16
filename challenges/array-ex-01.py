# Check if string_a is an anagram of string_b! (without taking the spaces into consideration)
# My solution:

def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    for k in s1:
        if k != " ":
            if k not in s2:
                return False

    for k in s2:
        if k != " ":
            if k not in s1:
                return False
    
    return True



string_a = 'public relations'
string_b = 'crap built on lies'

print(anagram(string_a, string_b))
print(anagram('go go go', 'gggooo'))
print(anagram('abc', 'cba'))
print(anagram('hi man', 'hi     man'))
print(anagram('123', '1 2'))


# Lecture solution 1:

def anagram_lecture1(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

# Lecture solution 2:

def anagram_lecture2(s1, s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge Case Check
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    
    return True