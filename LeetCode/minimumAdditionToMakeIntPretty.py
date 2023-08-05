class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        numTrailingZeros = 1
        numToAdd = 0

        while target < sum([int(i) for i in str(n + numToAdd)]):
            numToAdd = 10**numTrailingZeros - (n % 10**numTrailingZeros)
            numTrailingZeros += 1

        return numToAdd