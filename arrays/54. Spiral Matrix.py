# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        #define boundaries
        top, left = 0, 0
        right = len(matrix[0])
        bottom = len(matrix)
        
        output = []
        
        while (top < bottom) and (left < right):
            
            #move from left -> right
            for col in range(left, right):
                output.append(matrix[top][col])
            top += 1
            
            #move from up -> down
            for row in range(top, bottom):
                output.append(matrix[row][right-1])
            right -= 1
            
            #base case for single-row or single column matrix
            if not ((top < bottom) and (left < right)):
                break
            
            #move from right -> left
            for col in range(right - 1, left - 1, -1):
                output.append(matrix[bottom - 1][col])
            
            bottom -= 1
            
            for row in range(bottom - 1, top - 1, -1):
                output.append(matrix[row][left])
            
            left += 1
        
        return output
