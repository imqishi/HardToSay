class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [n for n in (cand1, cand2) if nums.count(n) > len(nums) // 3]

obj = Solution()
print obj.majorityElement([1,2,3,1,1,1])
