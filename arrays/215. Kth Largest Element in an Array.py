# https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Quick Select
        #this works based on the intuition that quicksort sorts one half of the array
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, pointer = nums[r], l
            
            for i in range (l, r):
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
                
            nums[r], nums[pointer] = nums[pointer], nums[r]
            
            if pointer > k:
                return quickSelect(l, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, r)
            else:
                return nums[pointer]
        
        return quickSelect(0, len(nums) - 1)
    
