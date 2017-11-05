class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        end = len(s) - 1
        max = end
        start = 0
        while start < end:
            while (start <= max) and not ((s[start].lower() >= 'a' and s[start].lower() <= 'z') or (s[start] >= '0' and s[start] <= '9')):
                start += 1
            while (end >= 0) and not ((s[end].lower() >= 'a' and s[end].lower() <= 'z') or (s[end] >= '0' and s[end] <= '9')):
                end -= 1

            if start >= end:
                return True

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1
        
        return True

obj = Solution()
print obj.isPalindrome('a.')