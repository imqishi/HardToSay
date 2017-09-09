class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(n):
            res.append([])
            for j in range(n):
                res[i].append(0)
        
        sums = n * n
        k = 1
        i = j = top = right = down = left = 0
        while k <= sums:
            # go right
            while j < n - right:
                res[i][j] = k
                k += 1
                j += 1
            j -= 1
            top += 1
            i += 1
            # go down
            while i < n - down:
                res[i][j] = k
                k += 1
                i += 1
            i -= 1
            right += 1
            j -= 1
            # go left
            while j >= left:
                res[i][j] = k
                k += 1
                j -= 1
            j += 1
            left += 1
            i -= 1
            # go up
            while i >= top:
                res[i][j] = k
                k += 1
                i -= 1
            i += 1
            down += 1
            j += 1

        return res

obj = Solution()
obj.generateMatrix(0)