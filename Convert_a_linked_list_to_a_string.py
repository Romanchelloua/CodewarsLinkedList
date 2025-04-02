def stringify(node):
    res_l = []
    el = node
    s = ''
    if el is None:
        return 'None'
    while el.next is not None:
        res_l.append(str(el.data))
        el = el.next
    res_l.append(str(el.data))
    s = ' -> '.join(res_l)
    s = s + ' -> None'
    return s