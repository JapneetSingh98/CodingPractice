class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = [nums[0], nums[1], nums[2]]
        for i in range(0, len(nums) - 2):
            lower = i + 1
            upper = len(nums) - 1
            while lower < upper:
                # print(i, lower, upper)
                cur = sum([nums[i], nums[lower], nums[upper]])
                if abs(target - cur) < abs(target - sum(closest)):
                    closest = [nums[i], nums[lower], nums[upper]]
                if cur < target:
                    while lower < upper:
                        lower += 1
                        if nums[lower] != nums[lower - 1]:
                            break
                elif cur == target:
                    return target
                else:
                    while lower < upper:
                        upper -= 1
                        if nums[upper] != nums[upper + 1]:
                            break

        return closest[0] + closest[1] + closest[2]