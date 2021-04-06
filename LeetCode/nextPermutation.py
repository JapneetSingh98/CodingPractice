class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        tail = [nums[len(nums)-1]]
        for i in range(1, len(nums)):
            tail.sort()
            for j in range(len(tail)):
                if tail[j] > nums[len(nums)-i-1]:
                    temp = tail[j]
                    tail[j] = nums[len(nums)-i-1]
                    nums[len(nums)-i-1] = temp
                    
                    tail.sort()
                    
                    nums[len(nums)-i:] = tail
                    return
            tail.append(nums[len(nums)-i-1])
                
        nums.sort()
        """
        Do not return anything, modify nums in-place instead.
        """