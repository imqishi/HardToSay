class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
        elif self.minStack[-1] >= x:
            self.minStack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return False

        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return False
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return False

        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print minStack.getMin()
minStack.pop()
print minStack.top()
print minStack.getMin()