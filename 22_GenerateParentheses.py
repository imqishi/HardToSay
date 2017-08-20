class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.backtrace("", 0, 0, n)

        return self.result

    def backtrace(self, str, left, right, n):
        if len(str) == n * 2:
            self.result.append(str)
            return

        if left < n:
            self.backtrace(str + "(", left+1, right, n)
        if right < left:
            self.backtrace(str + ")", left, right+1, n)

obj = Solution()
print obj.generateParenthesis(3)
