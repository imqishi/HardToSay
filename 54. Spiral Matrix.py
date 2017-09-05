class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        yLen = len(matrix)
        if yLen == 0:
            return []

        xLen = len(matrix[0])
        nums = xLen * yLen
        top = right = down = left = 0
        res = []
        i = j = p = 0
        while p < nums:
            # go right
            while j < xLen - right:
                res.append(matrix[i][j])
                p += 1
                j += 1
            j -= 1
            right += 1
            top += 1
            if p >= nums:
                break

            # go down
            i += 1
            while i < yLen - down:
                res.append(matrix[i][j])
                p += 1
                i += 1
            i -= 1
            down += 1
            if p >= nums:
                break

            # go left
            j -= 1
            while j >= left:
                res.append(matrix[i][j])
                p += 1
                j -= 1
            j += 1
            left += 1
            if p >= nums:
                break

            # go up
            i -= 1
            while i >= top:
                res.append(matrix[i][j])
                p += 1
                i -= 1
            i += 1
            if p >= nums:
                break

            # pre-go 1 step
            j += 1

        
        return res

obj = Solution()
print obj.spiralOrder([[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]])