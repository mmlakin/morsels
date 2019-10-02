def add(*lists):
    result=[]
    for a,b in zip(*lists):
        l=[]
        for x,y in zip(a,b):
            l+=[x+y]
        result.append(l)
    return result
