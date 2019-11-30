
def tail(sequence, n):
    nullvalue = object()
    l = [nullvalue] * n
    for x in sequence:
        l.append(x)
        l.pop(0)
    return [ y for y in l if y != nullvalue ]
