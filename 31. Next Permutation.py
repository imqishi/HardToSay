import copy
class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        origin = copy.copy(nums)
        if nums.sort(reverse = True) == origin:
            return nums.sort()

        watch = nums[1:]
        watch_bak = copy.copy(nums)
        if watch_bak.sort(reverse = True) == watch:
            nums[0], nums[1] = nums[1], nums[0]
            return nums

        i = 0
        while i < len(watch):
            i += 1

    def permutationByRecursion(self, nums, start = 0):
        if start >= len(nums) - 1:
            print nums
            return
        else:
            i = start
            while i < len(nums):
                nums[i], nums[start] = nums[start], nums[i]
                self.permutationByRecursion(nums, start+1)
                nums[i], nums[start] = nums[start], nums[i]
                i += 1

    def permOnebyOne(self, nums):
        end = len(nums) - 1
        reverse = True
        swap_pos = False
        while end > 0:
            if nums[end-1] < nums[end]:
                reverse = False
                swap_pos = end - 1
                break
            else:
                end -= 1
                continue

        if reverse is True:
            nums.sort()
        else:
            i = swap_pos + 1
            bak_pos = False
            while i < len(nums):
                if nums[i] > nums[swap_pos]:
                    if bak_pos is False:
                        bak_pos = i
                    else:
                        bak_pos = i if nums[i] <= nums[bak_pos] else bak_pos
                i += 1

            nums[swap_pos], nums[bak_pos] = nums[bak_pos], nums[swap_pos]
            bak = nums[swap_pos+1:]
            bak.reverse()
            nums[swap_pos+1:] = bak
            print nums



obj = Solution()
#obj.permutationByRecursion([1,2,3,4])
print obj.permOnebyOne([2,3,1,3,3])
