def bStrictlyAscending(a):

    prev = None
    for i in range(len(a)):
        if(i % 2 == 0):
            if(prev != None and a[i//2] <= prev):
                return False
            prev = a[i//2]
        else:
            if (prev != None and a[len(a) - 1 - (i // 2)] <= prev):
                return False
            prev = a[len(a) - 1 - (i // 2)]

    return True
