class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    head_ptr = head
    prev = None
    def rec(prev, ptr):
        if ptr is None:
            return prev
        temp = ptr.next
        ptr.next = prev
        prev = ptr
        return rec(prev, temp)
    return rec(prev, head_ptr)