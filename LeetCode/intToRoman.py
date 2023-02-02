class Solution:
    def intToRoman(self, num: int) -> str:
        options = [('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M', 'ERROR_', 'ERROR_')]
        solution = ""
        opt = 0
        while num > 0:
            cur = num%10
            num = num//10
            string = ""
            if cur == 0:
                pass
            elif cur < 4:
                string = options[opt][0] * cur
            elif cur == 4:
                string = options[opt][0] + options[opt][1]
            elif cur == 5:
                string = options[opt][1]
            elif cur < 9:
                string = options[opt][1] + options[opt][0] * (cur-5)
            else:
                string = options[opt][0] + options[opt][2]
            solution = string + solution

            opt += 1
            print(solution)
        return solution