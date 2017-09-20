class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end = len(digits) - 1
        digits[end] = digits[end] + 1
        remainder = digits[end] / 10
        digits[end] %= 10
        if remainder == 0:
            return digits
        end -= 1
        while end >= 0:
            digits[end] += remainder
            remainder = digits[end] / 10
            if remainder == 0:
                return digits
            digits[end] %= 10
            end -= 1

        if remainder != 0:
            digits = [remainder] + digits
        
        return digits

obj = Solution()
print obj.plusOne([1,2,3,9,9])