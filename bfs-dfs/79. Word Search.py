# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
          
        move_x = [-1, 1, 0, 0]
        move_y = [0, 0, -1, 1]
        direction = [(-1, 0), (1, 0),(0, -1),(0, 1)]
        R = len(board)
        C = len(board[0])

        visited = set()

        def dfs(row, col, word_index):

            if not (0 <= row < R and 0 <= col < C):
                return False

            if (row, col) in visited or board[row][col] != word[word_index]:
                return False

            if word_index == len(word) - 1:
                return True

            visited.add((row, col))
            for x, y in direction:
                new_r, new_c= row + x, col + y
                if dfs(new_r, new_c, word_index + 1):
                    return True

            visited.remove((row, col))
            return False



        for r in range(R):
            for c in range(C):
                # if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
