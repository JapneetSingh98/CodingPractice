class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0
        
        i = 0
        j = len(height) - 1
        
        while i < j:
            if min(height[i], height[j]) * (j-i) > largest:
                largest = min(height[i], height[j]) * (j-i)
                
            if height[i] < height[j]:
                i = i + 1
            elif height[j] < height[i]:
                j = j - 1
            else:
                i = i + 1
                j = j - 1
        
        return largest