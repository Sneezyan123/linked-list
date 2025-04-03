from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if not node or index<0:
        raise Exception()
    for i in range(index):
        
        node = node.next
        if node is None:
            raise Exception()
    return node
    # Your code goes here.
    