# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        count, i = 1, 0
        
        for j in range(1,len(nums)):
            if count == 1:
                count = 2 if nums[i] == nums[j] else 1
                i += 1
                nums [i], nums[j] = nums[j], nums[i]
            else:
                if nums[i] != nums[j]:
                    i += 1
                    nums [i], nums[j] = nums[j], nums[i]
                    count = 1
        return i + 1    
