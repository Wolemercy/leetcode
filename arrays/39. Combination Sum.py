# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    
    def dfs(self, nums, target, combo, res):
        if target == 0:
            res.append(combo[:])
            return
        
        if target < 0:
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], combo + [nums[i]], res)
