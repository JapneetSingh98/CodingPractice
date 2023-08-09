class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxSum = curSum

        for i in range(1, len(nums) - k + 1):
            curSum = curSum - nums[i - 1] + nums[i + k - 1]
            maxSum = max(maxSum, curSum)

        return maxSum / k