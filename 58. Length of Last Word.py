class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        arr = s.split(' ')
        
        return 0 if len(arr) == 0 else len(arr[-1])

obj = Solution()
print obj.lengthOfLastWord('w a tf ')