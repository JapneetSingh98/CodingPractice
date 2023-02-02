class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkBigger(s, list):
            newList = []
            for item in list:
                if item[1] <= 0 or item[2] >= len(s) - 1:
                    continue
                elif s[item[1] - 1] == s[item[2] + 1]:
                    newList.append((item[0] + 2, item[1] - 1, item[2] + 1))
                else:
                    continue
            if len(newList) == 0:
                return list
            return checkBigger(s, newList)

        curLargestPalindromes = []
        for i in range(0, len(s)):
            curLargestPalindromes.append((1, i, i))
            if i + 1 < len(s) and s[i] == s[i + 1]:
                curLargestPalindromes.insert(0, (2, i, i + 1))

        curLargestPalindromes = checkBigger(s, curLargestPalindromes)

        return s[curLargestPalindromes[0][1]:curLargestPalindromes[0][2] + 1]