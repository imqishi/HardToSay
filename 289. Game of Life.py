import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        bak = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = self.checkLife(bak, i, j)
        
        return board
        
    def checkLife(self, board, i, j):
        iLen = len(board)
        jLen = len(board[0])
        iSub, iAdd, jSub, jAdd = i - 1, i + 1, j - 1, j + 1
        hit = 0
        if iSub >= 0:
            if jSub >= 0 and board[iSub][jSub] == 1:
                hit += 1
            if board[iSub][j]  == 1:
                hit += 1
            if jAdd < jLen and board[iSub][jAdd] == 1:
                hit += 1
        if jSub >= 0 and board[i][jSub] == 1:
            hit += 1
        if jAdd < jLen and board[i][jAdd] == 1:
            hit += 1
        if iAdd < iLen:
            if jSub >= 0 and board[iAdd][jSub] == 1:
                hit += 1
            if board[iAdd][j]  == 1:
                hit += 1
            if jAdd < jLen and board[iAdd][jAdd] == 1:
                hit += 1

        if board[i][j] == 1:
            if hit < 2:
                return 0
            elif hit == 2 or hit == 3:
                return 1
            else:
                return 0
        else:
            if hit == 3:
                return 1
            else:
                return 0

obj = Solution()
print obj.gameOfLife([[1,1,1], [1,0,0], [0,1,1]])