import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.subCombine(n, k, 0, [])
        return self.res
    
    def subCombine(self, n, k, start, curArr):
        if len(curArr) == k:
            self.res.append(copy.copy(curArr))
            return

        for i in range(start + 1, n+1):
            curArr.append(i)
            self.subCombine(n, k, i, curArr)
            curArr.pop()

obj = Solution()
print obj.combine(4,2)