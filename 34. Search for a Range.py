class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        pivot = False
        while start <= end:
            pos = (start + end) / 2
            if nums[pos] == target:
                pivot = pos
                break
            elif nums[pos] < target:
                start = pos + 1
            else:
                end = pos - 1

        if pivot is False:
            return [-1, -1]

        before = after = pivot
        while before >= 0 and nums[before] == target:
            before -= 1

        while after < len(nums) and nums[after] == target:
            after += 1

        return [before+1, after-1]

a = Solution()
print a.searchRange([], 8)