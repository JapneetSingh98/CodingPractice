class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterClippings = {}
        for i in range(len(magazine)):
            if magazine[i] in letterClippings:
                letterClippings[magazine[i]] += 1
            else:
                letterClippings[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in letterClippings or letterClippings[ransomNote[i]] == 0:
                return False
            else:
                letterClippings[ransomNote[i]] -= 1

        return True