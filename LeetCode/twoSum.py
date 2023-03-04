class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        indexOf = {}

        for i in range(len(nums)):
            if target-nums[i] in indexOf:
                return [indexOf[target-nums[i]], i]
            else:
                indexOf[nums[i]] = i