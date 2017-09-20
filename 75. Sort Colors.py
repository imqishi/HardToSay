class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        
        print nums

    def sortColorsH(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while True:
            while nums[i] < 1:
                i += 1
            while nums[j] > 1:
                j -= 1
            
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[j], nums[0] = nums[0], nums[j]
        
        print nums

obj = Solution()
obj.sortColorsH([2,0,2,1,0,1])