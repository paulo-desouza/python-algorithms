# About to find out what is a BIG O notation. 

# Constant function:

def func_constant(values):
    print(values[0])

l = [1, 2, 3, 4]
func_constant(l)

# Always taking only one constant step size, no matter what the list size is.
# List of N items will always just print 1 item.
#
# -- -- -- 
#
# Linear function:

def func_list(l):

    for val in l:
        print(val)

# scales linearly with N.
#
# -- -- -- 
#
# Quadratic function:

def func_quad(l):

    for item_1 in l:
        for item_2 in l:
            print(item_1, item_2)

# Here, each item in the list will get looped and printed N times, where N is the list size.
# For N = 10, this will take 100 steps. Dangerous!
# 
# -- -- --
# 
# Another Linear Function

def print_2(l):

    for val in l:
        print(val)

    for val in l:
        print(val)
#
# -- -- --
#

def comp(l):

    print(l[0])  #O(1)

    midpoint = len(l)/2  #O(n/2)
    for val in l[:midpoint]:  
        print(val)

    for x in range(10):  #O(10)
        print('hello world')

# Even though there are different values, it all boils down to O(n) because these values are all constant.
# O(1 + n/2 + 10)   ==>    O(n)
#
#-- -- --
#

def matcher(l, match):
    for item in l:
        if item == match:
            return True

    return False

# In this function, there is a best case cenario if the match parameter is met inside the given list. If this is true, its a Constant Time Complexity. 
#
# -- -- --
# 

def create_list(n):
    new_list = []

    for num in range(n):
        new_list.append('new')

    return new_list

# Scales in memory with N

def printer(n):
    for x in range(10):
        print('Hello World!')

# Time complexity: 0(N)
# Space complexity: 0(1)
#
# -- -- --
#
#