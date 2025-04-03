def stringify(node):
    text = []
    head_ptr = node
    while True:
        val = head_ptr.data if head_ptr is not None else None
        text.append(str(val))
        if head_ptr is None:
            break
        head_ptr = head_ptr.next
    return " -> ".join(text)