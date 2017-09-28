class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 0
        res = []
        while i < (1 << n):
            res.append(i ^ (i >> 1))
            i += 1
        
        return res

obj = Solution()
print obj.grayCode(2)