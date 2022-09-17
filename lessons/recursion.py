# RECURSION

# Used as a technique in which a function makes one or more calls to itself

# Also used when a data structure uses smaller instances of the exact same type of data structure when it represents itself.

# Recursion provides a powerful alternative for performing repetitions of tasks in which a loop is not ideal.

# Factorial function example

def fact(n):

    if n == 0:
        return 1 

    else:
        return n * fact(n-1)

print(fact(5))