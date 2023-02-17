class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        print(nums)
        cur = nums[0]
        maxVal = nums[0]
        for i in range(1, len(nums)):
            print(cur)
            cur = max(nums[i], cur + nums[i])
            if cur > maxVal:
                maxVal = cur
        print(cur)
        return maxVal