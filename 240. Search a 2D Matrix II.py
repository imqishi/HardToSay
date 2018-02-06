class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)   
        if row == 0:
            return False
        col = len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
        
        return False