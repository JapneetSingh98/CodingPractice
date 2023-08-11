def solution(arr):
    output = 0
    curStretch = 0
    goingDown = 3
    if arr[0] > arr[1]:
        goingDown = 1
        curStretch = 1
    elif arr[0] < arr[1]:
        goingDown = 2
        curStretch = 1

    for i in range(2, len(arr)):
        if arr[i-1] == arr[i]:
            output += (curStretch * (curStretch + 1) / 2)
            curStretch = 0
            goingDown = 3
        elif (arr[i-1] < arr[i] and goingDown == 2) or (arr[i-1] > arr[i] and goingDown == 1):
            output += (curStretch * (curStretch + 1) / 2)
            curStretch = 1
        else:
            if arr[i-1] > arr[i]:
                goingDown = 1
            else:
                goingDown = 2
            curStretch += 1
    output += (curStretch * (curStretch + 1) / 2)
    return output