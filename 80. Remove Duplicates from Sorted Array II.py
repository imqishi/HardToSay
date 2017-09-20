class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        count = 1
        lastInt = nums[0]
        subCount = 1
        for i in xrange(1, l):
            if lastInt == nums[i]:
                if subCount >= 2:
                    continue
                else:
                    nums[count] = nums[i]
                    subCount += 1
                    count += 1
            if lastInt != nums[i]:
                nums[count] = nums[i]
                lastInt = nums[i]
                subCount = 1
                count += 1
        #print nums
        return count

obj = Solution()
print obj.removeDuplicates([1,1,1,1,1])