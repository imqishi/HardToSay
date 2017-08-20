class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {
            "(": ")",
            ")": "(",
            "{": "}",
            "}": "{",
            "[": "]",
            "]": "["
        }
        stack = []
        for ch in s:
            if len(stack) == 0 or stack[-1] != map[ch]:
                stack.append(ch)
            else:
                stack.pop()

        return len(stack) == 0

obj = Solution()
print obj.isValid("[{{([]))}]")