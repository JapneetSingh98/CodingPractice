class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        furthestBack = -1
        lastPos = {}
        for i in range(len(s)):
            #print(lastPos)
            if s[i] not in lastPos:         # first time seeing the character
                thisLen = i - furthestBack
                if thisLen > maxLength:
                    maxLength = thisLen
                
                lastPos[s[i]] = i
            
            else:                           # character has been seen before
                if lastPos[s[i]] < furthestBack:  # treat as if first time seeing character
                    thisLen = i - furthestBack
                    if thisLen > maxLength:
                        maxLength = thisLen
                
                    lastPos[s[i]] = i
                
                else:                               # need to adjust furthest back
                    thisLen = i - lastPos[s[i]]
                    if thisLen > maxLength:
                        maxLength = thisLen
                    
                    furthestBack = lastPos[s[i]]
                    lastPos[s[i]] = i
                    
        return maxLength