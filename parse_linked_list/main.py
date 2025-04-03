def linked_list_from_string(s):
    text = s.split(" -> ")
    head = Node(None)
    head_ptr = head
    for i in text:
        if(i == "None"):
            break
        val = Node(int(i))
        head_ptr.next = val
        head_ptr = val
    return head.next