import sys
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nlen = len(nums)
        if nlen < 4:
            return []

        nums.sort()
        i = 0
        result = []
        keys = {}
        while i < nlen - 3:
            if i > 0 and nums[i] == nums[i-1] and nums[i+1] == nums[i]:
                i += 1
                continue
            j = i + 1
            while j < nlen - 2:
                l, r = j + 1, nlen - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        key = str(nums[i]) + '-' + str(nums[j]) + '-' + str(nums[l]) + '-' + str(nums[r])
                        if key not in keys:
                            keys[key] = 1
                            result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l-1] == nums[l] and l < r:
                            l += 1
                        while nums[r+1] == nums[r] and l < r:
                            r -= 1

                j += 1
            i += 1

        return result


obj = Solution()
print obj.fourSum([1,1,1,2,2,3,3,3,7], 10)
