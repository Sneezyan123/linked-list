def loop_size(node):
    slow = node.next
    fast = node.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    q = 1
    slow = slow.next
    while slow != fast: 
        slow = slow.next
        q+=1 
    return q 