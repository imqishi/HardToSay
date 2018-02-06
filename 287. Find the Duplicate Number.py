class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 1:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow

obj = Solution()
print obj.findDuplicate([1,2,3,5,4,2])