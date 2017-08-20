class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        pivot = 0
        while start <= end:
            pos = (start + end) / 2
            if nums[pos] < nums[pos-1]:
                pivot = pos
                break
            else:
                if nums[pos] < nums[0]:
                    end = pos - 1
                else:
                    start = pos + 1

        nums = nums[pivot:] + nums[0:pivot]

        start, end = 0, len(nums) - 1
        while start <= end:
            pos = (start + end) / 2
            if nums[pos] == target:
                return (pos + pivot) % len(nums)
            elif nums[pos] < target:
                start = pos + 1
            else:
                end = pos - 1

        return -1

a = Solution()
print a.search([3,1], 3)
