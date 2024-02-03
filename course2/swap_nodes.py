'''
Given a linked list, swap the two nodes present at position `i` and `j`, assuming `0 <= i <= j`. The positions are based on 0-based indexing.

**Note:** You have to swap the nodes and not just the values. 

**Example:**
* `linked_list = 3 4 5 2 6 1 9`
* `positions = 2 5`
* `output = 3 4 1 2 6 5 9`

**Explanation:** 
* The node at position 3 has the value `2`
* The node at position 4 has the value `6`
* Swapping these nodes will result in a final order of nodes of `3 4 5 6 2 1 9`
'''

def swap_nodes(head, left_index, right_index):
    
    if left_index == right_index:
        return
    
    cur_node = head
    
    node_1 = None
    pre_node_1 = None
    
    node_2 = None
    pre_node_2 = None
    
    for idx in range(1, left_index+1):
        pre_node_1 = cur_node
        cur_node = cur_node.next
        node_1 = cur_node.next

    cur_node = head

    for idx in range(1, right_index+1):
        pre_node_2 = cur_node
        cur_node = cur_node.next
        node_2 = cur_node
        next_node_2 = cur_node.next
        
    pre_node_1.next = node_2
    pre_node_2.next = node_1
    
    temp = node_1.next
    node_1.next = node_2.next
    node_2.next = temp           