class Solution(object):
    def __init__(self):
        self.op = ['+', '-', '*', '/']

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        stack = []
        op = '+'
        s = s.lstrip()
        s = s.rstrip()
        for (i, ch) in enumerate(s):
            if ch == ' ':
                continue
            if ch not in self.op:
                num = num * 10 + int(ch)
            if ch in self.op or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    t = stack.pop()
                    if t < 0:
                        t = -t
                        stack.append(-(t / num))
                    else:
                        stack.append(t / num)
                num = 0
                op = ch

        return sum(stack)

obj = Solution()
print obj.calculate('14-3/2')