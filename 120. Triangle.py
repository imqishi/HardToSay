class Solution(object):
    def minimumTotal(self, triangle):
        """
        Use DP
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = []
        deepest = len(triangle) - 1
        if deepest == 0:
            return triangle[0][0]
        if deepest < 0:
            return 0
        # init
        for x in triangle[deepest]:
            res.append(x)

        for i in range(deepest, 0, -1):
            for j in range(i):
                res[j] = min(res[j] + triangle[i-1][j], res[j+1] + triangle[i-1][j])

        return res[0]


    def minimumTotalByDFS(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.level = len(triangle)
        if self.level == 0:
            return 0
        if self.level == 1:
            return triangle[0][0]

        self.triangle = triangle
        self.total = False
        self.calc(0, 0, 0)
        return self.total
    
    def calc(self, pos, cur_level, sum):
        sum += self.triangle[cur_level][pos]
        if cur_level == self.level - 1:
            if self.total is False:
                self.total = sum
            elif self.total > sum:
                self.total = sum
            return

        self.calc(pos, cur_level + 1, sum)
        self.calc(pos+1, cur_level + 1, sum)

obj = Solution()
print obj.minimumTotal([[1],[2,3],[2,1,3]])
print obj.minimumTotalByDFS([[1],[2,3],[2,1,3]])