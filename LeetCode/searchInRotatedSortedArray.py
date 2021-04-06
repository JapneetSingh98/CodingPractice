class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target >= nums[0]:
            i = 0
            while i < len(nums) and target >= nums[i]:
                if target == nums[i]:
                    return i
                else:
                    i += 1
            return -1
        else:
            i = len(nums)-1
            while i > 0 and target <= nums[i]:
                if target == nums[i]:
                    return i
                else:
                    i -= 1
            return -1