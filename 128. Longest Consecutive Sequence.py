class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        Max = 0
        for x in nums:
            if x in numMap:
                continue
            left = 0 if (x - 1) not in numMap else numMap[x-1]
            right = 0 if (x + 1) not in numMap else numMap[x+1]

            numMap[x] = left + right + 1
            if numMap[x] > Max:
                Max = numMap[x]

            numMap[x-left] = numMap[x]
            numMap[x+right] = numMap[x]
        
        return Max

obj = Solution()
print obj.longestConsecutive([100, 4, 200, 1, 3, 2])