class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        i = 0
        while i < len(matrix):
            if matrix[i][0] == 0:
                col0 = 0
            j = 1
            while j < len(matrix[0]):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                j += 1
            i += 1
        
        i = len(matrix) - 1
        while i >= 0:
            j = len(matrix[0]) - 1
            while j >= 1:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                j -= 1
            if col0 == 0:
                matrix[i][0] = 0
            i -= 1
