#Problem: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        _max = -inf
        
        while left != right:
            if height[left] <= height[right]:
                _max = max(_max, height[left] * (right - left))
                left += 1
            else:
                _max = max(_max, height[right] * (right - left))
                right -= 1
        return _max
