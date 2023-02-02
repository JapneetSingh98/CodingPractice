class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        if len(nums) < 3:
            return []
        for i in range(0, len(nums)-2):
            lower = i+1
            upper = len(nums)-1
            while lower < upper:
                #print(i, lower, upper)
                sum = nums[i] + nums[lower] + nums[upper]
                if sum < 0:
                    while lower < upper:
                        lower += 1
                        if nums[lower] != nums[lower-1]:
                            break
                elif sum == 0:
                    if [nums[i], nums[lower], nums[upper]] in output:
                        while lower < upper:
                            lower += 1
                            if nums[lower] != nums[lower-1]:
                                break
                        while lower < upper:
                            upper -= 1
                            if nums[upper] != nums[upper+1]:
                                break
                        pass
                    else:
                        output.append([nums[i], nums[lower], nums[upper]])
                        while lower < upper:
                            lower += 1
                            if nums[lower] != nums[lower-1]:
                                break
                        while lower < upper:
                            upper -= 1
                            if nums[upper] != nums[upper+1]:
                                break
                else:
                    while lower < upper:
                        upper -= 1
                        if nums[upper] != nums[upper+1]:
                            break
        return output