
def weightCapacity(weights, maxCapacity):
    weights.sort()
    return helper(weights, maxCapacity, cur)

def helper(weights, maxCapacity, cur):
    if cur > maxCapacity:
        return float('-inf')
    elif len(weights) == 0:
        return cur
    else:
        return max(weights[1:], maxCapacity, cur+weights[0]), weights[1:], maxCapacity, cur)
