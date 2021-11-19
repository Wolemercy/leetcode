# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows = [False] * R
        columns = [False] * C
        row_1 = False
        
       
        for c in range(C):
            if matrix[0][c] == 0:
                row_1 = True
                break
       
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 
                    if r != 0:
                        matrix[r][0] = 0
        
        for r in range(1, R):
            for c in range(1, C):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        
        if matrix[0][0] == 0:
            for r in range(R):
                matrix[r][0] = 0
        if row_1:
            for c in range(C):
                matrix[0][c] = 0
        
        return matrix
                
