# def solution(a, k):
#     # print(a)
#     # print(k)
#     numPairs = 0
#     modK = {}
#     # print(numPairs, modK)
#
#     for num in a:
#         opposite = k - num % k if num % k != 0 else 0
#         # print(num, opposite)
#         if str(opposite) in modK:
#             numPairs += modK[str(opposite)]
#
#         if str(num % k) in modK:
#             modK[str(num % k)] += 1
#         else:
#             modK[str(num % k)] = 1
#
#         # print(numPairs, modK)
#     return numPairs


def solution(a, k):
    output = 0
    modK = {}

    for i in range(len(a)):
        inverse = k - a[i] % k if a[i] % k != 0 else 0
        output += modK.get(str(inverse), 0)

        if str(a[i] % k) in modK:
            modK[str(a[i] % k)] += 1
        else:
            modK[str(a[i] % k)] = 1

    return output