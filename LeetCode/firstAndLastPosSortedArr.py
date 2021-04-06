class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        minimum = 0
        maximum = len(nums)-1
        mid = int((minimum+maximum)/2)
        
        while maximum - minimum > 1:
            if nums[mid] > target:
                maximum = mid
                mid = int((minimum+maximum)/2)
            elif nums[mid] < target:
                minimum = mid
                mid = int((minimum+maximum)/2)
            else:
                minimum = mid
                while minimum-1 >= 0 and nums[minimum-1] == target:
                    minimum -= 1
                maximum = mid
                while maximum+1 <= len(nums)-1 and nums[maximum+1] == target:
                    maximum += 1
                return [minimum, maximum]
        if nums[minimum] == target and nums[maximum] == target:
            return [minimum, maximum]
        elif nums[minimum] == target:
            return [minimum, minimum]
        elif nums[maximum] == target:
            return [maximum, maximum]
        return [-1, -1]