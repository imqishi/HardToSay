import copy
class Solution(object):
    result = []
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        used = [ False ] * len(nums)
        self.sub_permute(nums, used, [])
        return self.result

    def sub_permute(self, nums, used, sub_result):
        if len(sub_result) == len(nums):
            self.result.append(copy.copy(sub_result))
            return

        i = 0
        while i < len(nums):
            if used[i] is False:
                if i > 0 and nums[i] == nums[i-1] and used[i-1] is False:
                    i += 1
                    continue
                sub_result.append(nums[i])
                used[i] =  True
                self.sub_permute(nums, used, sub_result)
                used[i] = False
                sub_result.pop()

            i += 1

obj = Solution()
#print obj.permuteUnique([1,1,3])
print obj.permuteUnique([1,0,1,1])