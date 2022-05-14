def array_diff(a, b):
    if(len(b) > 0):
        for i in range(0,len(a)):
            for x in range(0,len(b)):
                if(b[x] in a):
                    a.remove(b[x])
        return a
    else:
        return a


print("Diff is",array_diff([1,2,3],[1,2]))


def array_diff(a, b):
    return [x for x in a if x not in b]