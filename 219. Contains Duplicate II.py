class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapper = {}
        for (index, num) in enumerate(nums):
            if num in mapper and index - mapper[num] <= k:
                return True
            mapper[num] = index
        
        return False


obj = Solution()
print obj.containsNearbyDuplicate([], 2)