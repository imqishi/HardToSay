class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = reach = 0
        while i < len(nums) and i <= reach:
            reach = max([ i + nums[i], reach])
            i += 1

        return i == len(nums)

    # If nums' value is exactly length it jumps
    # This will be right
    def canJumpWrong(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True

        # init dp array
        dp = []
        for index, length in enumerate(nums):
            dp.append(index + length)

        # dp
        i = 2
        while i <= len(nums) - 1:
            j = 0
            while j < len(nums) - 1:
                if dp[j] >= len(nums) - 1:
                    break
                if dp[j] + nums[dp[j]] >= len(nums) - 1:
                    dp[j] = dp[j] + nums[dp[j]]
                    break
                dp[j] = dp[j] + nums[dp[j]]
                j += 1
            i += 1

        if dp[0] >= len(nums) - 1:
            return True

        return False
    
    def canJumpByDFS(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.ok = False
        self.dfs(nums, 0)
        return self.ok

    def dfs(self, nums, start):
        if self.ok:
            return
        if start == len(nums) - 1:
            self.ok = True
            return
        if start + nums[start] >= len(nums) - 1:
            self.ok = True
            return
        if nums[start] == 0:
            return

        i = 1
        while i <= nums[start]:
            self.dfs(nums, start + i)
            i += 1

obj = Solution()
print obj.canJump([0,2,3])
print obj.canJump([2,5,0,0])
print obj.canJump([1,2,3])
print obj.canJump([2,3,1,1,4])
print obj.canJump([3,2,1,0,4])
#print obj.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])