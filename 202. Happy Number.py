class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mapper = { n: True }
        s = str(n)

        sub_sum = 0
        while sub_sum != 1:
            sub_sum = 0
            for c in s:
                sn = int(c)
                sub_sum += sn * sn
            if sub_sum != 1 and sub_sum in mapper:
                return False
            mapper[sub_sum] = True
            s = str(sub_sum)
        
        return True

obj = Solution()
print obj.isHappy(1)