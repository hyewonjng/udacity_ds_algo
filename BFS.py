from collections import deque
# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
    
    # set value of the node
    def set_value(self,value):
        self.value = value
    
    # get value of the node
    def get_value(self):
        return self.value
    
    # set a node for the left child
    def set_left_child(self,left):
        self.left = left
    
    # set a node for the right child
    def set_right_child(self, right):
        self.right = right
        
    # get the node of left child
    def get_left_child(self):
        return self.left
    
    # get the node of right child
    def get_right_child(self):
        return self.right

    # check if node has left child -> return boolean
    def has_left_child(self):
        return self.left != None
    
    # check if node has right child -> return boolean
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"
        
def bfs(tree):
    visited_order = list()
    node = tree.get_root()
    queue = Queue()
    que = node.enq()
    visited_order.append(que)

    while node:
        if node.has_left_child():
            node = node.get_left_child()
            node.enq()
            visited_order.append(node)
        
        if node.has_right_child():



