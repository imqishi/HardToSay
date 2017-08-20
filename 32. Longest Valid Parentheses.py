class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        curMax = 0
        result = [0] * len(s)
        i = 1
        while i < len(s):
            if s[i] == ')':
                if s[i-1] == '(':
                    result[i] = result[i-2] + 2 if (i - 2) >= 0 else 2
                    curMax = max(result[i], curMax)
                else:
                    if i - result[i-1] - 1 >= 0 and s[i-result[i-1]-1] == '(':
                        result[i] = result[i-1] + 2 + (result[i-result[i-1]-2] if i - result[i-1] - 2 >= 0 else 0)
                        curMax = max(result[i], curMax)

            i += 1

        return curMax

obj = Solution()
print obj.longestValidParentheses(")(((((()())()()))()(()))(")