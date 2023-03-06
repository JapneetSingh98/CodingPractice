class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}

        for num in nums:
            if num in appeared:
                return True
            appeared[num] = 1
        return False