class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        res = [0] * (n + 1)
        for i in citations:
            if i > n:
                res[n] += 1
            else:
                res[i] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += res[i]
            if total >= i:
                return i
        
        return 0