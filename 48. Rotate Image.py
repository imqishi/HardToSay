class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        length = len(matrix)
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            i += 1
        print matrix

obj = Solution()
print obj.rotate([[1,2,3], [4,5,6], [7,8,9]])