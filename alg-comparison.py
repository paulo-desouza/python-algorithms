# Both these algorithms have the same funcionality, so we are comparing them on Jupyter Notebook with the %timeit command.

def sum1(n):    # 223 ns ± 9.45 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    final_sum = 0

    for x in range(n+1):
        final_sum += x
    
    return final_sum


def sum2(n):        #60 ns ± 0.625 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
    return (n*(n+1))/2


# Conclusion: The second function was way faster, but there is a better way of measuring these times, since these are dependent on hardware.
# Next step: Big-O Notation 

