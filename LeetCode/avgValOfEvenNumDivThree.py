class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        totSum = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                totSum += num
                count += 1

        if count == 0:
            return 0
        return totSum // count