class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                nums[i] += nums[i]
                nums[i+1] = 0
            if nums[i] == 0:
                count += 1

        return list(filter(lambda x: x != 0, nums)) + [0 for i in range(count)]