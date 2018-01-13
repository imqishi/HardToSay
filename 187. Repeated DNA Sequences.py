class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mapper = {}
        if len(s) < 11:
            return []

        for i in range(0, len(s) - 10 + 1):
            key = s[i:i + 10]
            mapper[key] = mapper[key] + 1 if key in mapper else 1
        
        rtn = []
        for key in mapper:
            if mapper[key] > 1:
                rtn.append(key)
        
        return rtn

obj = Solution()
print obj.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
print obj.findRepeatedDnaSequences('AAAAAAAAAAA')