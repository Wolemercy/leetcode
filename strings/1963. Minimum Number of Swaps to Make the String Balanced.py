# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        count=0
        for char in s:
            if count and char != '[':
                count -= 1
            else:
                count += 1
                
        return (count + 1) //2
