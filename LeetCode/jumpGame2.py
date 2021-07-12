class Solution:
    def jump(self, nums: List[int]) -> int:
        numJumps = [float('inf')] * len(nums)
        
        numJumps[len(nums)-1] = 0
        
        for pos in range(len(nums)-2, -1, -1):
            numJumps[pos] = min(numJumps[pos: pos+nums[pos]+1]) + 1

        return numJumps[0]