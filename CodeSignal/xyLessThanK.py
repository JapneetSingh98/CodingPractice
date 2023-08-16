def solution(a, b, k):
    count = 0

    for i in range(len(a)):
        aVal = None
        if b[len(b) - 1 - i] // 10000 > 0:
            aVal = a[i] * 100000
        elif b[len(b) - 1 - i] // 1000 > 0:
            aVal = a[i] * 10000
        elif b[len(b) - 1 - i] // 100 > 0:
            aVal = a[i] * 1000
        elif b[len(b) - 1 - i] // 10 > 0:
            aVal = a[i] * 100
        else:
            aVal = a[i] * 10

        if aVal + b[len(b) - 1 - i] < k:
            count += 1

    return count