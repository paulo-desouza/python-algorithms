# Find the Missing Element

# Consider an array of non-negative integers. a second array is formed 
# by shuffling the elements of the first array and removing a random element.
# Given these two elements, find which element is missing in the current array:

# My solution:
import collections

def missing_number(arr1, arr2):
    missingno = ''
    for i in arr1:
        if i not in arr2:
            missingno = str(i)
    
    print(f'The missing number is {missingno}!')



array1 = [1,2,3,4,5,6]
array2 = [3,4,5,6,1]
missing_number(array1, array2)

# Lecture solution:

def finder(arr1, arr2):

    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1


# Lecture Solution 2:

    def finder2(arr1, arr2):
        d = collections.defaultdict(int)

        for num in arr2:
            d[num]+= 1

        for num in arr1:
            if d[num] == 0:
                return num
            else:
                d[num] -= 1