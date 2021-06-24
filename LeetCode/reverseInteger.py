class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        output = ''
        
        for char in strX:
            output = char + output
            
        if x < 0:
            output = '-' + output[:-1]
        
        if int(output) > 2**31 - 1 or int(output) < - (2**31):
            return 0
        return int(output)