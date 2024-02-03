'''
Find and return the `nth` row of Pascal's triangle in the form a list. `n` is 0-based.

For example, if `n = 4`, then `output = [1, 4, 6, 4, 1]`.

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
'''

def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n == 0:
        return [1]
    
    cur_row = [1]
    
    for row in range(1, n+1):
        prev_row = cur_row
        cur_row = [1]
        
        for idx in range(1, row):
            num = prev_row[idx-1]+prev_row[idx]
            cur_row.append(num)
        
        cur_row.append(1)
        
    return cur_row