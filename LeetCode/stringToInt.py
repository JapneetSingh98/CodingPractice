class Solution:
    def myAtoi(self, s: str) -> int:
        value = 0
        negative = False
        for i in range(0, len(s)):
            if s[i] not in [' ', '-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 0
            if s[i] == '-':
                negative = True
                s = s[i + 1:]
                break
            if s[i] == "+":
                s = s[i + 1:]
                break
            if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                s = s[i:]
                break

        for i in range(0, len(s)):
            print(value, s[i])
            if s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            value = value * 10 + ord(s[i]) - ord('0')

        if negative:
            if 0 - value < -2 ** 31:
                return -2 ** 31
            return 0 - value
        if value > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return value