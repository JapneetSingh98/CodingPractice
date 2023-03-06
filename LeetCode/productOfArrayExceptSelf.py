class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        indexZeros = []
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                indexZeros.append(i)
                if len(indexZeros) == 2:
                    return [0] * len(nums)
            else:
                prod *= nums[i]

        output = []
        if len(indexZeros) > 0:
            for num in nums:
                if num == 0:
                    output.append(prod)
                else:
                    output.append(0)
        else:
            for num in nums:
                output.append(prod // num)

        return output