class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # init dp
        dp = []
        m = len(obstacleGrid)
        if m == 0:
            return 0
        if m == 1:
            try:
                obstacleGrid[0].index(1)
                return 0
            except:
                return 1
        else:
            n = len(obstacleGrid[0])

        for i in range(m):
            dp.append([])
            for j in range(n):
                if i == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i].append(0)
                    elif j > 0 and dp[i][j-1] == 0:
                        dp[i].append(0)
                    else:
                        dp[i].append(1)
                elif j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i].append(0)
                    elif i > 0 and dp[i-1][j] == 0:
                        dp[i].append(0)
                    else:
                        dp[i].append(1)
                else:
                    dp[i].append(0)
        
        # let's go...
        i = 1
        while i < m:
            j = 1
            while j < n:
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                j += 1
            i += 1

        return dp[m-1][n-1]

obj = Solution()
print obj.uniquePathsWithObstacles([[0],[0]])
print obj.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
print obj.uniquePathsWithObstacles([[1],[0]])