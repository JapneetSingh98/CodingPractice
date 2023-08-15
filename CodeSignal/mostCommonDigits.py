def solution(a):
    count = [0] * 10

    for num in a:
        count[num % 10] += 1
        if num // 10 > 0:
            count[num // 10] += 1

    output = []
    maxCount = 0

    for i in range(len(count)):
        if count[i] > maxCount:
            maxCount = count[i]
            output = [i]
        elif count[i] == maxCount:
            output.append(i)

    return output
