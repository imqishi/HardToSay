class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            t = list(s)
            t.sort()
            key = ''.join(t)
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]
        
        return [ result[i] for i in result]

obj = Solution()
obj.groupAnagrams(['abc', 'bac'])