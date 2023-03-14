class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            return min(self.findMin(nums[0:len(nums)//2]), self.findMin(nums[len(nums)//2:len(nums)]))