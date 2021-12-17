# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = maxLength = 0
        usedChar = {}
        
        for i, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
                
            
            maxLength = max(maxLength, i - start + 1)
            usedChar[char] = i
            
        
        return maxLength
                
        
