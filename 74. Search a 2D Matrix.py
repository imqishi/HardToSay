class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cols = len(matrix)
        if cols == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        start, end = 0, cols - 1
        while start <= end:
            medium = (start + end) / 2
            if matrix[medium][0] == target or matrix[start][0] == target or matrix[end][0] == target:
                return True
            elif matrix[medium][0] > target:
                end = medium - 1
            else:
                start = medium + 1

        if matrix[medium][0] > target:
            if medium > 0:
                medium -= 1
            else:
                return False
        
        start, end = 0, len(matrix[medium]) - 1
        while start <= end:
            i = (start + end) / 2
            if matrix[medium][i] == target or matrix[medium][start] == target or matrix[medium][end] == target:
                return True
            elif matrix[medium][i] > target:
                end = i - 1
            else:
                start = i + 1

        return False

obj = Solution()
print obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 5)