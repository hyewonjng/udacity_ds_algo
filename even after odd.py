'''
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. **Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.** 

**Example:**
* `linked list = 1 2 3 4 5 6`
* `output = 1 3 5 2 4 6`
'''

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    cur_node = head
    
    odd_head = None
    odd_tail = None
    even_head = None
    even_tail = None
    
    while cur_node:
        if cur_node.data %2 == 0: #even
            if even_head is None and even_tail is None:
                even_head = cur_node
            else: 
                even_tail.next = cur_node
                
            even_tail = cur_node
            cur_node = cur_node.next
                
        else: # odd
            if odd_head is None and odd_tail is None:
                odd_head = cur_node
            else:
                odd_tail.next = cur_node
            odd_tail = cur_node
            cur_node = cur_node.next
    if odd_head is None:
        return even_head
    
    odd_tail.next = even_head
    return odd_head
                
            
    