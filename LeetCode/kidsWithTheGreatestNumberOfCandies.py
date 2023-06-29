class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = [False] * len(candies)

        greatest = max(candies) - extraCandies

        for i in range(len(candies)):
            output[i] = candies[i] >= greatest

        return output
