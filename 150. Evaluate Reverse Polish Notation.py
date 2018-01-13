class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for i in tokens:
            if i == '+' or i == '-' or i == '*' or i == '/':
                val2 = nums.pop()
                val1 = nums.pop()
                value = self.calc(i, val1, val2)
                nums.append(value)
                last_is_op = True
            else:
                nums.append(i)

        if len(nums) > 0:
            value = int(nums[0])
        return value
    
    def calc(self, op, val1, val2):
        val1 = int(val1)
        val2 = int(val2)
        if op == '+':
            return val1 + val2
        elif op == '-':
            return val1 - val2
        elif op == '*':
            return val1 * val2
        elif op == '/':
            return val1 / val2

obj = Solution()
print obj.evalRPN(["2", "1", "+", "3", "*"])
print obj.evalRPN(["4", "13", "5", "/", "+"])
print obj.evalRPN(["5", "1", "2", "+", "4", "*", "+", "3", "-"])
print obj.evalRPN(["3","11","5","+","-"])
print obj.evalRPN(["4","-2","/","2","-3","-","-"])
print obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])