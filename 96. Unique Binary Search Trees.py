class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        res = []
        for i in xrange(n+1):
            res.append(0)
        res[0] = 1

        for len in xrange(1, n+1):
            for j in xrange(len):
                res[len] += res[j] * res[len-j-1]
        
        return res[n]

obj = Solution()
print obj.numTrees(1)