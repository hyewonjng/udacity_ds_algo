'''
You are given the head of a linked list and two integers, `i` and `j`.
You have to retain the first `i` nodes and then delete the next `j` nodes. Continue doing so until the end of the linked list. 

**Example:**
* `linked-list = 1 2 3 4 5 6 7 8 9 10 11 12`
* `i = 2`
* `j = 3` 
* `Output = 1 2 6 7 11 12` 
'''

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    if head is None:
        return
    
    if i < 0 or j < 0:
        return
    
    if i == 0 or j == 0:
        return

    cur_node = head
    new_next = head
    
    while cur_node:
        for idx in range(i-1): # range(1)
            cur_node = cur_node.next 
            new_next = new_next.next
            
        for idx in range(j+1):
            if new_next.next is not None:
                new_next = new_next.next
            else:
                new_next = None
                break
    
        cur_node.next = new_next
        cur_node = new_next