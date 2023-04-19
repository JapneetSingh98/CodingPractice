def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1

    maxArea = 0

    while (left < right):
        curArea = (right - left) * min(height[left], height[right])
        if (curArea > maxArea):
            maxArea = curArea

        if (height[left] < height[right]):
            left += 1
        else:
            right -= 1

    return maxArea