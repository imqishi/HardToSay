class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for num in nums:
            ta = ( ~a & b & num ) | ( a & ~b & ~num )
            b=( ~a & ~b & num ) | ( ~a & b & ~num )
            a=ta

        return a | b

obj = Solution()
print obj.singleNumber([1,1,1,2,2])
