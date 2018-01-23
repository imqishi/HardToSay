class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort(reverse = True)
        return nums[k - 1]
    

obj = Solution()
print obj.findKthLargest([], 0)