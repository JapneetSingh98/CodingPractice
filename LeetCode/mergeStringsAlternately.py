class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        length = min(len(word1), len(word2))

        for i in range(length):
            output += word1[i] + word2[i]

        if len(word1) > len(word2):
            output += word1[length:]
        elif len(word1) < len(word2):
            output += word2[length:]

        return output