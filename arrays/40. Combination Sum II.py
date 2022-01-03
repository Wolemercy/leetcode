# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        combo  = []
        candidates.sort()
        self.backtrack(candidates, target, 0, combo, res)
        return res
        
    def backtrack(self, nums, target, index, combo, res):
        if target == 0:
            res.append(combo[:])
        
        if target < 0:
            return
        
        prev = -1
        for i in range(index, len(nums)):
            
            if prev == nums[i]:
                continue
            
            combo.append(nums[i])
            self.backtrack(nums, target - nums[i], i + 1, combo, res)
            combo.pop()
            
            prev = nums[i]
