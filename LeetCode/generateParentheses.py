def helper(numOpen, numClose, curStr):
    #print(numOpen, numClose)
    if numOpen < 0 or numClose < 0:
        return []
        
    if numOpen > numClose:
        return []
        
    if numClose == 0:
        #print(curStr)
        return [curStr]
        
    return helper(numOpen-1, numClose, curStr+'(') + helper(numOpen, numClose-1, curStr+')')

class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        numOpen = n
        numClose = n
        
        outputList = helper(numOpen, numClose, "")
        
        return outputList