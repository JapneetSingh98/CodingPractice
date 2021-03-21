class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = []
        for i in range(numRows):
            rows.append("")
        
        cur = 0
        up = False
        for i in range(len(s)):
            rows[cur] = rows[cur] + s[i]
            if cur == 0:
                up = False
                cur = cur + 1
            elif cur == numRows - 1:
                up = True
                cur = cur - 1
            elif up:
                cur = cur - 1
            else:
                cur = cur + 1
        
        output = ""
        
        for row in rows:
            output = output + row
        
        return output