# string compression

# given a string in the form 'AAABBBBBCCCCCDDEEEE' compress it to become 'A3B5C5D2E4'
# should be case-sensitive


def compress(str):

    new_str = ''


    for k, i in enumerate(str):

        c = 1
        if i != str[k-1] or i == 0:
            while str[k+c] == str[k]:
                
            
                new_str += f'{i}{c}'
                print(new_str)
        
    print(new_str)


compress('AAABBBBCCCCCDDEEEE')
