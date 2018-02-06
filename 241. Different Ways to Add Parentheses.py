class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for (i, ch) in enumerate(input):
            if ch == '+' or ch == '-' or ch == '*':
                left = input[:i]
                right = input[i+1:]
                left_res = self.diffWaysToCompute(left)
                right_res = self.diffWaysToCompute(right)
                for num1 in left_res:
                    for num2 in right_res:
                        num = 0
                        if ch == '+':
                            num = num1 + num2
                        elif ch == '-':
                            num = num1 - num2
                        elif ch == '*':
                            num = num1 * num2
                        res.append(num)
        
        if len(res) == 0:
            res.append(int(input))

        return res

obj = Solution()
print obj.diffWaysToCompute('1+2*3')