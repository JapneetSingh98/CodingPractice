class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        if len(nums) < 4:
            return []
        for x in range(0, len(nums)-3):
            for i in range(x+1, len(nums)-2):
                lower = i+1
                upper = len(nums)-1
                while lower < upper:
                    #print(i, lower, upper)
                    sum = nums[x] + nums[i] + nums[lower] + nums[upper]
                    if sum < target:
                        while lower < upper:
                            lower += 1
                            if nums[lower] != nums[lower-1]:
                                break
                    elif sum == target:
                        if [nums[x], nums[i], nums[lower], nums[upper]] in output:
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
                            output.append([nums[x], nums[i], nums[lower], nums[upper]])
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