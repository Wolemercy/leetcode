# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        output = []
        
        def backtrack(arr, index):
            if index == len(nums):
                output.append(arr[:])
                return
            
            arr.append(nums[index])
            
            
            if arr not in output:
                backtrack(arr, index + 1)

            arr.pop()
            
            backtrack(arr, index + 1)
            
        
        backtrack([], 0)
        
        return output
