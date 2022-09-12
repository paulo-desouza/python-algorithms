# Array Pair Sum

# Given an integer array, output all the unique pairs that sum up to a specific value k.
# The input: pair_sum([1,3,2,2], 4)
# would return 2 pairs: (1,3) (2,2)

# My solution:

       
def pair_sum(arr, value):

    pair_counter = 0
    pair_list = []

    for key1, item1 in enumerate(arr):
        for key2, item2 in enumerate(arr):
            if key1 == key2:
                pass

            else:
                if item1 + item2 == value:
                    
                    if ([item1, item2] not in pair_list) and ([item2, item1] not in pair_list):
                        pair_list.append([item1, item2])
                        pair_counter += 1

    return print(pair_list, pair_counter)
                    


""" pair_sum([1,3,2,2], 4)
pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
pair_sum([1,2,3,1],3)
pair_sum([1,3,2,2],4) """
    

# Lecture Solution:

def lecture_pair_sum(arr, k):

    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:

        target = k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add(((min(num, target)), max(num,target)))

    print('\n'.join(map(str, list(output))))

lecture_pair_sum([1,3,2,2], 4)