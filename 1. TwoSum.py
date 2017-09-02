class Solution(object):
    # this is time O(n^2) space O(1)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        length = len(nums)
        while i < length:
            j = i + 1
            while j < length:
                if(nums[i] + nums[j] == target):
                    return [ i, j ]
                j += 1
            i += 1

        return False

    # this is time and space are all O(n)
    def twoSum1(self, nums, target):
        i = 0
        length = len(nums)
        map = {}
        while i < length:
            left = target - nums[i]
            if(map.has_key(left) == True):
                return [ map[left], i ]
            map[nums[i]] = i
            i += 1


obj = Solution()
print obj.twoSum([3,2,4], 6)
print obj.twoSum1([3,2,4], 6)