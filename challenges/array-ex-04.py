# Largest Continuous Sum

# Given an array of integers (positive and negative) find the largest continuous sum.

def largest_sum(arr):
    counter = 0
    largest = 0
    for key, item in enumerate(arr):
        largest += item


    for i in range(len(arr)-1, -1, -1):

        largest_test = largest - arr[i]
        
        if largest_test > largest:
            largest = largest_test
    

    
    print('-----')
    print(largest_test)

        

my_list = [1,2,-1,3,4,10,10,-10,-1]  #29


largest_sum(my_list)
largest_sum([1,2,-1,3,4,-1])
largest_sum([-1,1])