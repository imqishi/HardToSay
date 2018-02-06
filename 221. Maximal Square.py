class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # init
        dp = []
        maxsize = 0
        for i in range(len(matrix)):
            dp.append([])
            for j in range(len(matrix[0])):
                if (i == 0 or j == 0) and matrix[i][j] == '1':
                    dp[i].append(1)
                    maxsize = max(maxsize, dp[i][j])
                else:
                    dp[i].append(0)

        if len(dp) == 0:
            return 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxsize = max(maxsize, dp[i][j])
        
        return maxsize * maxsize

    def maximalSquareOp1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # init
        pre = cur = []
        maxsize = 0
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                pre[i].append(1)
                maxsize = max(maxsize, pre[i][0])
            else:
                pre[i].append(0)

        if len(pre) == 0:
            return 0

        for j in range(1, len(matrix[0])):
            cur[0] = matrix[0][j] - '0'
            maxsize = max(maxsize, cur[0])
            for i in range(1, len(matrix)):
                if matrix[i][j] == '1':
                    cur[i] = min(cur[i - 1], pre[i - 1], pre[i]) + 1
                    maxsize = max(maxsize, cur[i])
            
            pre, cur = cur, pre
            cur = [0] * len(matrix)
        
        return maxsize * maxsize

    def maximalSquareOp2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [0] * (m + 1)
        maxsize = pre = 0;
        for j in range(n):
            for i in range(1, m + 1):
                temp = dp[i]
                if matrix[i - 1][j] == '1':
                    dp[i] = min(dp[i], min(dp[i - 1], pre)) + 1
                    maxsize = max(maxsize, dp[i])
                else:
                    dp[i] = 0
                pre = temp

        return maxsize * maxsize

obj = Solution()
print obj.maximalSquare([['1']])