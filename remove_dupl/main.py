class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    head_ptr = head
    if head is None:
        return head
    while(head_ptr.next is not None):
        node = head_ptr
        while(node.data == head_ptr.data):
            head_ptr = head_ptr.next
            if head_ptr is None:
                node.next = None
                return head
        node.next = head_ptr
    return head