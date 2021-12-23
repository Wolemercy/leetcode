# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #using backtracking
        
        result = []
        
        def backtrack(arr, index):
            
            #base case
            if index == len(nums):
                result.append(arr[:])
                return
            
            arr.append(nums[index])
            
            backtrack(arr, index + 1)
            
            arr.pop()
            
            backtrack(arr, index + 1)
        
        backtrack([], 0)
        return result

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #using a loop
        
        output = [[]]
        
        for num in nums:
            output += [arr + [num] for arr in output]
        
        return output
        
                      
            
        
        
        
        
        
        
