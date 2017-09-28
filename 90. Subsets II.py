import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        max = len(nums)
        self.res = [[]]
        for i in xrange(max+1):
            j = 0
            while j < len(nums):
                if j != 0 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                self.dfs(nums, i, j, [nums[j]])
                j += 1

        return self.res

    def dfs(self, nums, level, start, tmp):
        if len(tmp) == level:
            self.res.append(copy.copy(tmp))
            return

        i = start + 1
        while i < len(nums):
            if i != start + 1 and nums[i] == nums[i-1]:
                i += 1
                continue
            tmp.append(nums[i])
            self.dfs(nums, level, i, tmp)
            tmp.pop()
            i += 1

obj = Solution()
obj.subsetsWithDup([1,2,2])