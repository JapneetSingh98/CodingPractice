class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        appearance = {}
        for n in nums:
            if n in appearance:
                del appearance[n]
            else:
                appearance[n] = 1
        
        return [*appearance][0]