# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #Recursive solution
        
#         def backtrack(nums, path=[], res=[]):
            
#             if not nums:
#                 res.append(path[:])
                
            
#             for i in range(len(nums)):
#                 newNums = nums[:i] + nums[i+1:]
#                 path.append(nums[i])
#                 backtrack(newNums, path, res)
#                 path.pop()
            
#             return res
        
#         return backtrack(nums)

        #Iterative solution
    
        stack = [(nums, [])]
        
        res = []
        
        
        while stack:
            arr, path = stack.pop()
            
            if not arr:
                res.append(path)
            
            for i in range(len(arr)):
                newNums = arr[:i] + arr[i+1:]
                stack.append((newNums, path+[arr[i]]))
        
        return res
