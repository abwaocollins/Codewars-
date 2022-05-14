def tribonacci(signature, n):
    if(n>2):
        for i in range(3,n):
            next = signature[-1]+signature[-2]+signature[-3]
            signature.append(next)
        return signature
    elif(n==1):
        del signature[1:]
        return  signature
    elif(n==2):
        del signature[2:]
        return signature
    else:
        return []

print(tribonacci([1, 1, 1], 2))


# second way
def tribonacci(signature,n):

    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]