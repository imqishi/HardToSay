class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapper = {}
        for ch in s:
            if ch in mapper:
                mapper[ch] += 1
            else:
                mapper[ch] = 1
        
        for ch in t:
            if ch not in mapper:
                return False
            mapper[ch] -= 1
            if mapper[ch] == 0:
                del mapper[ch]
        
        if len(mapper) == 0:
            return True
        return False

obj = Solution()
print obj.isAnagram('abc', 'cba')
print obj.isAnagram('abc', 'sba')
print obj.isAnagram('abc', 'cbad')
print obj.isAnagram('', '')