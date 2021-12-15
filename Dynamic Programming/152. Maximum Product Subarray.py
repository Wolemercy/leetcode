# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
                 
        res = nums[0]
        
        
        maxNum, minNum = 1, 1
        
        for num in nums:
            
            tempMax = num * maxNum
            tempMin = num * minNum
            
            maxNum = max(num, tempMax, tempMin)
            
            minNum = min(num, tempMax, tempMin)
            
            res = max(res, maxNum)
        
        return res
