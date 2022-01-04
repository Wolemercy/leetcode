# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        
        nums = [i for i in range(1, 10)]

        def backtrack(index, depth, combo, total):
            if depth == k:
                if total == n:
                    res.append(combo[:])
                return
            
            elif depth > k or total > n or index >= 9:
                return
            
            for i in range(index, 9):
                combo.append(nums[i])
                # print(nums[i])
                
                backtrack(i + 1, depth + 1, combo, total + nums[i])
                print(depth)
                combo.pop()
                # depth -= 1
        
        backtrack(0, 0, [], 0)
        return res
