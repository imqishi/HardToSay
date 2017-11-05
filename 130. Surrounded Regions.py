class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.zeroDict = {}
        rows = len(board)
        if rows > 0:
            cols = len(board[0])
        else:
            return

        # From first row left to right
        for j in range(cols):
            if board[0][j] == 'O':
                self.expand(board, rows, cols, 0, j)
        # From first column top to down
        for i in range(1, rows):
            if board[i][0] == 'O':
                self.expand(board, rows, cols, i, 0)
        # From last row left to right
        for j in range(1, cols):
            if board[rows - 1][j] == 'O':
                self.expand(board, rows, cols, rows - 1, j)
        # From last column top to down
        for i in range(1, rows - 1):
            if board[i][cols - 1] == 'O':
                self.expand(board, rows, cols, i, cols - 1)
        
        for i in range(rows):
            for j in range(cols):
                key = str(i) + '-' + str(j)
                if key not in self.zeroDict:
                    board[i][j] = 'X'

        print board

    def expand(self, board, rows, cols, i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != 'O':
            return
        key = str(i) + '-' + str(j)
        if key in self.zeroDict:
            return
        self.zeroDict[key] = 1

        self.expand(board, rows, cols, i - 1, j)
        self.expand(board, rows, cols, i + 1, j)
        self.expand(board, rows, cols, i, j - 1)
        self.expand(board, rows, cols, i, j + 1)
    

obj = Solution()
#obj.solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']])
#obj.solve([['X', 'O', 'X', 'X']])
#obj.solve([["X","O","X"],["X","O","X"],["X","O","X"]])
obj.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])