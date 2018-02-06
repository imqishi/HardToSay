class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        res = [1]
        count2 = count3 = count5 = 0
        for i in range(1, n):
            res.append(min(res[count2] * 2, res[count5] * 5, res[count3] * 3))
            if res[i] == res[count2] * 2:
                count2 += 1
            if res[i] == res[count3] * 3:
                count3 += 1
            if res[i] == res[count5] * 5:
                count5 += 1
        
        return res[-1]