# exercise 1: Generate Factorials

def prod(a,b):
    # TODO change output to the product of a and b
    output = a * b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i +=1
        n = output 

# Test cases
fact_res = fact_gen()
num = 5
for i in range(num):
    print(next(fact_res))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120
    
# Excercise 2: 
    # Define a function check_sudoku() here:
def check_sudoku(square):
    # each column
    col_list = []

    for i in range(len(square)):
        col_list.append(square[i][0])
        diagnal_list.append(square[i][i])

    vertical_list.sort()
    diagnal_list.sort()

    print(first_list)
    print(vertical_list)
    print(diagnal_list)

    if first_list == vertical_list == diagnal_list:
        return True
    else:
        return False


    
# Test cases
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]
incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]
incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]
incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]
incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]
incorrect5 = [ [1, 1.5],
               [1.5, 1]]

print(check_sudoku(correct))
#>>> True   
print(check_sudoku(incorrect))
#>>> False
print(check_sudoku(incorrect2))
#>>> False
print(check_sudoku(incorrect3))
#>>> False
print(check_sudoku(incorrect4))
#>>> False
print(check_sudoku(incorrect5))
#>>> False