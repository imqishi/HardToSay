import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        gap = sys.maxint
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = sum - target
                tg = abs(diff)
                if tg < gap:
                    gap = tg
                    result = sum
                if gap == 0:
                    return sum

                if diff < 0:
                    left += 1
                elif diff > 0:
                    right -= 1

        return result

obj = Solution()
print obj.threeSumClosest([0,0,0], -5)