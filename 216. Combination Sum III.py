class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.rtn = []
        for i in range(1, 10):
            self.subCom(k - 1, n - i, i, [ i ])
        return self.rtn
    
    def subCom(self, k, n, cur, arr):
        if k == 0:
            if n == 0:
                self.rtn.append(arr[:])
            return

        for i in range(cur + 1, 10):
            arr.append(i)
            self.subCom(k - 1, n - i, i, arr)
            arr.pop()
        return

obj = Solution()
print obj.combinationSum3(3, 15)