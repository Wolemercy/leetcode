# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        combo = []
        
        def backtrack(o, c):
            
            if o == c == n:
                
                res.append("".join(combo))
            
            if o < n:
                combo.append("(")
                backtrack(o + 1, c)
                combo.pop()
            
            if c < o:
                combo.append(")")
                backtrack(o, c + 1)
                combo.pop()
            
            
        
        backtrack(0, 0)
        return res
