class Solution(object):
    def maxProduct(self, nums):
        curMax = nums[0]
        ongoingMax = nums[0]
        ongoingMin = nums[0]
        print(ongoingMax, ongoingMin)
        
        for i in range(1,len(nums)):
            tempOngMax = max(nums[i], nums[i] * ongoingMax, nums[i] * ongoingMin)
            ongoingMin = min(nums[i], nums[i] * ongoingMax, nums[i] * ongoingMin)
            ongoingMax = tempOngMax

            curMax = max(curMax, ongoingMax)

        return curMax