class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Construct triple-tuples
        res = []
        for (index, str) in enumerate(board):
            second = []
            for i in range(len(str) / 3):
                second.append({})
            for (jndex, ch) in enumerate(str):
                if ch == '.':
                    continue
                second[jndex/3][ch] = True
            res.append(second)

        # After that, we only need to compare triple-tuples
        # Test row
        for row in board:
            test = {}
            for ch in row:
                if ch == '.':
                    continue
                if ch in test:
                    return False
                else:
                    test[ch] = True
        # Test column
        rowLen = len(board)
        colLen = len(board[0])
        for i in range(colLen):
            test = {}
            for j in range(rowLen):
                if board[j][i] == '.':
                    continue
                if board[j][i] in test:
                    return False
                else:
                    test[board[j][i]] = True
        # Test 9-cell
        test = {}
        rowLen = len(res)
        colLen = len(res[0])
        for i in range(colLen):
            for j in range(rowLen):
                if j == 0 or j % 3 == 0:
                    test = {}
                keys = res[j][i].keys()
                for k in keys:
                    if k in test:
                        return False
                    else:
                        test[k] = True

        return True



a = Solution()
print a.isValidSudoku([".........","...3..5..",".........","...8.....","....116..",".........","......1..","........7",".......4."])
