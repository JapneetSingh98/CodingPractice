def solution(a, k):
    # print(a)
    # print(k)
    numPairs = 0
    modK = {}
    # print(numPairs, modK)

    for num in a:
        opposite = k - num % k if num % k != 0 else 0
        # print(num, opposite)
        if str(opposite) in modK:
            numPairs += modK[str(opposite)]

        if str(num % k) in modK:
            modK[str(num % k)] += 1
        else:
            modK[str(num % k)] = 1

        # print(numPairs, modK)
    return numPairs