import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = []
        m = len(grid)
        if m == 0:
            return 0
        if m == 1:
            return sum(grid[0])

        n = len(grid[0])
        for i in range(m):
            dp.append([])
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i].append(grid[0][0])
                elif i == 0:
                    dp[i].append(dp[i][j-1] + grid[i][j])
                elif j == 0:
                    dp[i].append(dp[i-1][j] + grid[i][j])
                else:
                    dp[i].append(sys.maxint)

        i = 1
        while i < m:
            j = 1
            while j < n:
                t1 = grid[i][j] + dp[i][j-1]
                t2 = grid[i][j] + dp[i-1][j]
                if t1 < t2:
                    dp[i][j] = t1
                else:
                    dp[i][j] = t2

                j += 1
            i += 1
        
        return dp[m-1][n-1]

obj = Solution()
print obj.minPathSum([[1,2,3],[2,3,5],[1,4,5]])