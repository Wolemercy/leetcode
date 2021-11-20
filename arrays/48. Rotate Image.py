# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #transposing and reflecting
        N = len(matrix)
        
        #transposing -> change rows to columns
        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        
        #reflecting -> swapping elements along each row from one end to the other
        
        for i in range(N):
            for j in range(N//2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
