class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        yLen = len(board)
        i = 0
        while i < yLen:
            j = 0
            while j < len(board[i]):
                if self.subExist(board, i, j, word):
                    return True
                j += 1
            i += 1
        return False
    
    def subExist(self, board, i, j, word):
        if 0 == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or word[0] != board[i][j]:
            return False
        t = board[i][j]
        board[i][j] = '#'
        e = self.subExist(board, i, j + 1, word[1:]) or self.subExist(board, i, j - 1, word[1:]) or self.subExist(board, i + 1, j, word[1:]) or self.subExist(board, i - 1, j, word[1:])
        board[i][j] = t
        return e

obj = Solution()
print obj.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCCED')