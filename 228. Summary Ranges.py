class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        res = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if end == nums[i] - 1:
                end = nums[i]
            else:
                if start != end:
                    res.append(str(start) + '->' + str(end))
                else:
                    res.append(str(start))
                start = end = nums[i]
        if start != end:
            res.append(str(start) + '->' + str(end))
        else:
            res.append(str(start))
            
        return res

obj = Solution()
print obj.summaryRanges([0,1,2,4,5,6,7,9])
print obj.summaryRanges([0,2,3,4,6,8,9])
print obj.summaryRanges([0])
print obj.summaryRanges([0,1])