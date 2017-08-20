class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums) - 1
        pos = False
        while start <= end:
            pos = (start + end) / 2
            if nums[pos] == target:
                break
            elif nums[pos] < target:
                start = pos + 1
            else:
                end = pos - 1

        if nums[pos] < target:
            return pos + 1
        else:
            before = pos
            while nums[pos] == nums[before] and before >= 0:
                before -= 1
            return before + 1


a = Solution()
print a.searchInsert([], 0)