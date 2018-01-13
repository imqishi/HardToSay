class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        self.rows = len(grid)
        if self.rows == 0:
            return 0
        self.cols = len(grid[0])
        for (i, row) in enumerate(grid):
            for (j, cell) in enumerate(row):
                if cell == "1":
                    num += 1
                    self.expand(grid, i, j)
        return num
    
    def expand(self, grid, i, j):
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        if i + 1 <= self.rows - 1:
            self.expand(grid, i + 1, j)
        if j + 1 <= self.cols - 1:
            self.expand(grid, i, j + 1)
        if i - 1 >= 0:
            self.expand(grid, i - 1, j)
        if j - 1 >= 0:
            self.expand(grid, i, j - 1)

obj = Solution()
print obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])