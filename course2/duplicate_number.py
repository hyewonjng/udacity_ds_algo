'''
You have been given an array of length = n. 
The array contains integers from 0 to n - 2. 
Each number in the array is present exactly once except for one number which is present twice. 
Find and return this duplicate number present in the array

Example:
arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)

The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).
'''

def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    
    # create a dictionary to count duplicates
    res_dict = {}
    
    for i in range(len(arr)):
        if arr[i] not in res_dict:
            key_name = arr[i]
            res_dict[arr[i]] = 1
        else:
            key_name = arr[i]
            res_dict[arr[i]] += 1
    
    for key, value in res_dict.items():
        if value >= 2:
            return key
        

# the given solution

def duplicate_number(arr):
    current_sum = 0
    expected_sum = 0

    for num in arr:
        current_sum += num

    for i in range(len(arr) - 1):
        expected_sum += i
        
    return current_sum - expected_sum
    
