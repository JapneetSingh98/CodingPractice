class Solution:
    alreadySeen = {}
    
    def helper(self, s:str) ->int:
        if s in self.alreadySeen:
            return self.alreadySeen[s]
        
        if len(s) == 0:
            return 1
        
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1
        
        if len(s) >= 2:
            if int(s[0:2]) < 27:
                outp = self.helper(s[1:]) + self.helper(s[2:])
            else:
                outp = self.helper(s[1:])
        
        self.alreadySeen[s] = outp
        return outp
        
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        return self.helper(s)