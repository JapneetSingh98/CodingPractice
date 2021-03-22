class Solution:
    def helper(self, digits, curOut):
        
        if len(digits) == 0:
            return curOut
        
        conv = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        out = []
        for x in curOut:
            for i in range(len(conv[int(digits[0]) - 2])):
                out.append(x + conv[int(digits[0]) - 2][i])
        if len(digits) == 1:
            return out
        
        return self.helper(digits[1:], out)
    
    def letterCombinations(self, digits: str) -> List[str]:
        out = self.helper(digits, [""])
        if out == [""]:
            return []
        return out
        