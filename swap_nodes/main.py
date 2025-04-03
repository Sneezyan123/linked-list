from preloaded import Node

def swap_pairs(head):

    ptr  = Node()
    ptr.next = head
    prev = ptr

    while prev.next and prev.next.next:
        q = prev.next
        s = prev.next.next
        q.next = s.next
        s.next = q
        prev.next = s
        prev = q

    return ptr.next