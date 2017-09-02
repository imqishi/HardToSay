class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_string = ""
        num = len(strs)
        if num < 1:
            return ""
        i = 0
        while True:
            if i >= len(strs[0]):
                break
            cur = strs[0][i]
            ok = True
            for j in range(1, num):
                if i >= len(strs[j]) or cur != strs[j][i]:
                    ok = False
                    break
            if ok is not True:
                break
            common_string += cur
            i += 1

        return common_string

obj = Solution()
print obj.longestCommonPrefix(["ascde","asc","as"])
