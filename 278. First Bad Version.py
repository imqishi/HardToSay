# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) / 2
            rtn = isBadVersion(mid)
            if rtn is True:
                right = mid
            else:
                left = mid + 1
        
        return left

    def isBadVersion(self, n):
        if n >= 3:
            return True
        else:
            return False

obj = Solution()
print obj.firstBadVersion(2)