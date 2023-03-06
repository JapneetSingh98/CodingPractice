class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMax = 0
        buyPrice = None

        for price in prices:
            if buyPrice == None or price < buyPrice:
                buyPrice = price
            else:
                curProfit = price - buyPrice
                if curProfit > curMax:
                    curMax = curProfit
        return curMax
