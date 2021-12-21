# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if len(nums) == 1 and nums[0] == target:
         #   return 0

        
        left, right = 0, len(nums) - 1
        
        
        while left <= right:
            
            mid = (right + left) // 2
            
            if nums[mid] == target:
                return mid
            
            
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                
                else:
                    left = mid + 1
                    print(left)
            
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
        
        return  -1
        
