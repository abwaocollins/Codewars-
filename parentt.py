def validBraces(string):
    open_b = ["(","{","["]
    closing = [")" , "}" , "]"]

    res =[]
    for st in string:
        if st in open_b:
            res.insert(0 ,st)
        elif st in closing:
            if len(res)==0:
                return False
            if res[0] == open_b[closing.index(st)]:
                res.pop(0)
            else:
                return False

    if len(res) == 0:
        return True
    else:
        return False


print(validBraces("[(){}(([])})]"))
