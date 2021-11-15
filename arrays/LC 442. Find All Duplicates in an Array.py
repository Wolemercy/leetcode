# https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        #negative marking of the index
        
        output = []
        for num in nums:
            curr = abs(num) - 1
            
            if nums[curr] < 0:
                output.append(abs(num))
                
            else:
                nums[curr] *= -1
        
        return output
