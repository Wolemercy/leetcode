# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
#         use backtracking properly

        res = []
        perm = []
        
        from collections import defaultdict
        _hash = defaultdict(int)
        # _hash = {n:0 for n in nums}
        for n in nums:
            _hash[n] += 1
        
        def dfs():
            
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in _hash:
                if _hash[n] > 0:
                    
                    perm.append(n)
                    _hash[n] -= 1
                    
                    dfs()
                    
                    perm.pop()
                    _hash[n] += 1
            return res
        
        return dfs()
            
