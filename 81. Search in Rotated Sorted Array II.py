class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            med = (start + end) / 2
            if nums[med] == target:
                return True
            if nums[med] > nums[end]:
                if nums[med] > target and nums[start] <= target:
                    end = med
                else:
                    start = med + 1
            elif nums[med] < nums[end]:
                if nums[med] < target and nums[end] >= target:
                    start = med + 1
                else:
                    end = med
            else:
                end -= 1
        
        return True if nums[start] == target else False

                    

    def searchSB(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            med = (start + end) / 2
            if nums[med] == target or nums[start] == target or nums[end] == target:
                return True
            if nums[med] < target:# med too small
                if nums[0] < nums[med]:# must go right
                    start = self.goRight(nums, med)
                    if start == False:
                        return False
                elif nums[0] > nums[med]:
                    if nums[0] > target:
                        start = self.goRight(nums, med)
                        if start == False:
                            return False
                    elif nums[0] < target:
                        end = self.goLeft(nums, med)
                        if end == False:
                            return False
                    else:
                        return True
                else:
                    t = self.goLeft(nums, med)
                    if t is not False:
                        end = t
                    else:
                        t = self.goRight(nums, med)
                        if t is False:
                            return False
                        else:
                            start = t
            else:# med too big
                if nums[0] > nums[med]:# go left
                    end = self.goLeft(nums, med)
                    if end == False:
                        return False
                elif nums[0] < nums[med]:
                    if nums[0] > target:
                        start = self.goRight(nums, med)
                        if start == False:
                            return False
                    elif nums[0] < target:
                        end = self.goLeft(nums, med)
                        if end == False:
                            return False
                    else:
                        return True
                else:
                    t = self.goLeft(nums, med)
                    if t is not False:
                        end = t
                    else:
                        t = self.goRight(nums, med)
                        if t is False:
                            return False
                        else:
                            start = t


        return False

    def goRight(self, nums, med):
        t = med
        while t < len(nums) and nums[t] == nums[med]:
            t += 1
        return t if t < len(nums) else False

    def goLeft(self, nums, med):
        t = med
        while t >= 0 and nums[t] == nums[med]:
            t -= 1
        return t if t >= 0 else False

obj = Solution()
print obj.search([1,3,1,1,1], 3)