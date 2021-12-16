# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        #using extra space and sorting first
        
        nums.sort()
        
        left, right = 0, len(nums) - 1
        output = []
        
        while left <= right:
            if left != right:
                output.append(nums[left])
                left += 1
                
                output.append(nums[right])
                right -= 1
            else:
                output.append(nums[left])
                break
                
        return output
            
