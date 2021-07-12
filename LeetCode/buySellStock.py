class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curProfit = 0
        curMin = float('inf')
        
        for i in range(len(prices)):
            
            curProfit = max(curProfit, prices[i]-curMin)
            curMin = min(curMin, prices[i])
        
        return curProfit