class Solution(object):
    def helpSearch(self, nums, start, end, target):
        if (end < start) or (end == start and nums[start] != target):
            return -1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        # end is now greater than start

        # non rotated subarray
        if nums[end] > nums[start]:

            # target not in range
            if target > nums[end] or target < nums[start]:
                return -1

            # target in range
            else:
                mid = (end + start) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return self.helpSearch(nums, start + 1, mid - 1, target)
                else:
                    return self.helpSearch(nums, mid + 1, end - 1, target)

        # rotated subarray
        else:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid

            return max(self.helpSearch(nums, start + 1, mid - 1, target),
                       self.helpSearch(nums, mid + 1, end - 1, target))

    def search(self, nums, target):
        return self.helpSearch(nums, 0, len(nums) - 1, target)