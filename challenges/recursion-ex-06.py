# FIBONACCI SEQUENCE

# Implement a fibonacci sequence using Recursion and Memoization.

# Your function will take a number N and return the Nth number of the fibonacci sequence.



def fib_iter(n):
    a = 0
    b = 1

    for i in range(n):
        a,b = b,a+b

    return a 

def fib_rec(n):

    #base case

    if n==0 or n==1:
        return n

    #recursive case

    else:
        return fib_rec(n-1) + fib_rec(n-2)


# Memoization! Set up the cache

n = 10
cache = [None]*(n+1)


def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n


    # Check Cache: if existant, return the result.
    if cache[n] != None:

        return cache[n]

    # Keep Setting Cache

    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]