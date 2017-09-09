class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # init dp, when i or j is 0 val = 1 else 0
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                if i == 0:
                    dp[i].append(1)
                elif j == 0:
                    dp[i].append(1)
                else:
                    dp[i].append(0)

        i = 1
        while i < m:
            j = 1
            while j < n:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                j += 1
            i += 1

        return dp[m-1][n-1]

    # In above solution, dp array we only use last one.
    # So we can only record by two column not a matrix
    def uniquePathsDP1(self, m, n):
        if m > n:
            m, n = n, m
        cur = [1] * m
        last = [1] * m
        j = 1
        while j < n:
            i = 1
            while i < m:
                cur[i] = cur[i-1] + last[j]
                i += 1
            cur, last = last, cur
            j += 1

        return last[m-1]

    # In above solution, we use two column and update 'last' by 'cur'
    # We can also need not an extra last...
    # Actually, last[j] is cur[i] that is updating
    def uniquePathsDP2(self, m, n):
        if m > n:
            m, n = n, m
        dp = [1] * m
        j = 1
        while j < n:
            i = 1
            while i < m:
                dp[i] += dp[i-1]
                i += 1
            j += 1
        
        return dp[m-1]

    def uniquePathsByDFS(self, m, n):
        self.nums = 0
        self.dfs(0, 0, m, n)
        return self.nums
        
    def dfs(self, i, j, m, n):
        if i == m-1 and j == n-1:
            self.nums += 1
            return
        if i < m:
            self.dfs(i+1, j, m, n)
        if j < n-1:
            self.dfs(i, j+1, m, n)

obj = Solution()
print obj.uniquePaths(3, 3)
print obj.uniquePathsByDFS(3, 3)