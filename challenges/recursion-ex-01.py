# Recursion exercises! 
# Given an integer (example 5), have your function return the sum between all the numbers counting towards 0. (5 + 4 + 3 + 2 + 1 = 15)

def recursive_sum(num):
    if num == 0:
        return num
    return num + recursive_sum(num-1)

print(recursive_sum(5))

# Given an integer 4321, return 4+3+2+1

def integer_separator(num, result=[]):

    if num == 0:
        final = ''
        result.reverse()
        final = '+'.join(result)
        return final

    else:
        result.append(str(num % 10))
        newnum = num // 10

    return integer_separator(newnum, result)


print(integer_separator(4321))

