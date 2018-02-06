class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        bucket = {}
        n = len(nums)
        
        for i in range(n):
            m = nums[i] / (t + 1)
            if m in bucket or (m - 1 in bucket and abs(nums[i] - bucket[m - 1]) < (t + 1)) or (m + 1 in bucket and abs(nums[i] - bucket[m + 1]) < (t + 1)):
                return True
            bucket[m] = nums[i]
            # delete first added num
            if i >= k:
                del bucket[nums[i - k] / (t + 1)]
        
        return False


obj = Solution()
print obj.containsNearbyAlmostDuplicate([], 2, 3)