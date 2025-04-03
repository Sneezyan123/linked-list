""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    head_ptr = head
    newNode = Node(data)
    if head_ptr is None:
        return newNode
    if head_ptr.data >= data:
        newNode.next = head_ptr
        return newNode
    while(head_ptr is not None):
        headnext = head_ptr.next.data if head_ptr.next is not None else 99999
        if(head_ptr.data <= data <= headnext):
            temp = head_ptr.next
            head_ptr.next = newNode
            newNode.next = temp
            return head
        head_ptr = head_ptr.next
    return head