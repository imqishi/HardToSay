class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return False
        start, end = 0, len(numbers) - 1
        while start != end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            if numbers[start] + numbers[end] < target:
                start += 1
            if numbers[start] + numbers[end] > target:
                end -= 1
        
        return False

obj = Solution()
print obj.twoSum([0,1,2,3,4,5,6,7], 5)