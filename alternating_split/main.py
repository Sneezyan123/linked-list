class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def push(head, data):
    i = head
    
    while i.next is not None:
        i = i.next
        
    i.next = Node(data)
    
    return head

def alternating_split(head):
    if not head or not head.next:
        raise Exception()
    ptr = head
    first = Node()
    second = Node()
    fptr = first
    sptr = second
    counter = 0
    while ptr is not None:
        
        if counter % 2 == 0:
            sptr.next = Node(ptr.data)
            sptr = sptr.next
        else:
            fptr.next = Node(ptr.data)
            fptr = fptr.next
        counter += 1
        ptr = ptr.next

    return Context(first.next, second.next)
