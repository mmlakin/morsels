def tail(seq,n):
    if n <= 0:
        return []
    null = object()
    l = [null] * n
    for x in seq:
        l.append(x)
        l.pop(0)
    return [
        y
        for y in l
        if y != null
    ]
