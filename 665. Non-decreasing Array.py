class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        times = 0
        for i in range(1, len(nums)):
            if times > 1:
                return False
            if nums[i] < nums[i-1]:
                bak = nums[i-1]
                nums[i-1] = nums[i]
                if i - 2 >= 0:
                    if nums[i-1] < nums[i-2]:
                        nums[i-1] = nums[i] = bak
                times += 1

        return times <= 1

        times = 0
        for i in range(1, len(nums)):
            if times > 1:
                return False
            if nums[i] < nums[i-1]:
                if i - 2 >= 0 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
                times += 1

        return times <= 1


obj = Solution()
print obj.checkPossibility([4, 2, 1])
print obj.checkPossibility([3, 4, 2, 3])
print obj.checkPossibility([3, 4, 4, 3])