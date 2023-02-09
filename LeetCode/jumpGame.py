class Solution:
    def canJump(self, nums: List[int]) -> bool:
        closestTrue = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= closestTrue:
                closestTrue = i

        return closestTrue == 0