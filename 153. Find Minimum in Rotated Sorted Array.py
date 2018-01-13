class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        if end == -1:
            return 0
        if end == 0:
            return nums[0]

        mid = (start + end) / 2
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
            mid = (start + end) / 2

        return nums[start]

obj = Solution()
print obj.findMin([3,4,5,6,0,1,2])
print obj.findMin([2,1])