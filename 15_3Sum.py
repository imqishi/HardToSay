class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 3:
            return []
        if nums[-1] < 0:
            return []
        if nums[-1] == 0 and nums[-3] == 0:
            return [[0,0,0]]
        if nums[0] == 0 and nums[2] == 0:
            return [[0,0,0]]
        # determine 0 bound
        i = left = right = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                left = i
                i += 1
                while i < len(nums):
                    if nums[i] != 0:
                        break
                    i += 1
                right = i - 1
                break
            elif nums[i] < 0 and nums[i+1] > 0:
                left = i
                right = i + 1
                break
            i += 1

        result = {}
        realLeft = left - 1 if nums[left] == 0 else left #this is left < 0 max pos
        realRight = right + 1 if nums[right] == 0 else right #this is right > 0 min pos
        i = 0
        while i <= realLeft:
            j = k = len(nums) - 1
            while j >= realRight:
                k = j - 1
                while k >= realRight:
                    if nums[j] + nums[k] < -nums[i]:
                        break
                    if nums[j] + nums[k] == -nums[i]:
                        result[str(nums[i])+'-'+str(nums[j])+'-'+str(nums[k])] = [nums[i], nums[j], nums[k]]
                    k -= 1
                j -= 1
            i += 1

        i = len(nums) - 1
        while i >= realRight:
            j = k = 0
            while j <= realLeft:
                k = j + 1
                while k <= realLeft:
                    if nums[j] + nums[k] > -nums[i]:
                        break
                    if nums[j] + nums[k] == -nums[i]:
                        result[str(nums[j])+'-'+str(nums[k])+'-'+str(nums[i])] = [nums[j], nums[k], nums[i]]
                    k += 1
                j += 1

            i -= 1

        if realRight - realLeft != 0:
            zeros = realRight - realLeft - 1
            # if zeros num is odd or at least 3 zeros
            # there may be more result
            if zeros >= 3:
                result['0-0-0'] = [0, 0, 0]
            if zeros >= 1:
                i = 0
                while i <= realLeft:
                    if -nums[i] in nums:
                        result[str(nums[i])+'-0-'+str(-nums[i])] = [nums[i], 0, -nums[i]]
                    i += 1

        realResult = []
        for i in result:
            realResult.append(result[i])
        return realResult


    def threeSumEasy(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] == 0:
                if i + 1 < len(nums) and i + 2 < len(nums):
                    if nums[i+1] == 0 and nums[i+2] == 0:
                        result.append([0,0,0])
                        break
                    else:
                        break
                else:
                    break
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -=1
        return result



obj = Solution()
print obj.threeSum([-1,0,1,2,-1,-4])
print obj.threeSumEasy([0,0,0])
