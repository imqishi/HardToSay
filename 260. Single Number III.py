class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mapper = {}
        for n in nums:
            if n not in mapper:
                mapper[n] = 1
            else:
                mapper[n] -= 1
            if mapper[n] == 0:
                del mapper[n]
        res = []       
        for n in mapper:
            res.append(n)
        return res

    def singleNumberByBinaryOp(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for n in nums:
            diff ^= n
        diff &= -diff
        
        ret = [0, 0]
        for n in nums:
            if n & diff == 0:
                ret[0] ^= n
            else:
                ret[1] ^= n
        
        return ret

obj = Solution()
print obj.singleNumber([1,1,2,2,3,4])
print obj.singleNumberByBinaryOp([1,1,2,2,3,4])