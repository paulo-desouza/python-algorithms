# string compression

# given a string in the form 'AAABBBBBCCCCCDDEEEE' compress it to become 'A3B5C5D2E4'
# should be case-sensitive


# My solution: Quadratic Time Complexity: not the most optimal! Check the lecture solution.
def compress(s):
    new_str = ''
    counter = 0
    for k, v in enumerate(s):
        if s[k] != s[k-1] or k == 0:

            while s[k] == s[k+counter]:
                
                if counter == 0: 
                    new_str += v
                    counter += 1

                else:
                    counter += 1
                
                if (k+counter) == len(s):
                    break

            new_str += str(counter)
            counter = 0
    print(new_str)



# Lecture Solution: 
# Linear Time Complexity
# compressing without checking!!

def compress2(s):

    # first check for edge cases!
    r = ''
    l = len(s)
    
    if l == 0:
        return ''

    if l == 1:
        return s+'1'

    last = s[0]
    cnt = 1
    i = 1

    while i < l:

        if s[i] == s[i-1]:
            cnt += 1
        else: 
            r = r + s[i-1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i-1] + str(cnt)

    print(r)

compress('AAABBbbCCCCCDDEEEE')
compress2('AAABBbbCCCCCDDEEEE')