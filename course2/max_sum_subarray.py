'''
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

Example 1:
arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.

Example 2:
arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
'''
# my answer

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    max_sum = 0
    
    for idx in range(len(arr)):
        cur_sum = arr[idx]
        
        for num2 in arr[idx+1:]:
            
            cur_sum += num2
            
            if cur_sum > max_sum:
                max_sum = cur_sum
    return max_sum

# given anwer

def max_sum_subarray(arr):
    
    current_sum = arr[0]  
    max_sum = arr[0]      

    for element in arr[1:]:
        current_sum = max(current_sum + element, element)
        max_sum = max(current_sum, max_sum)   
    
    return max_sum