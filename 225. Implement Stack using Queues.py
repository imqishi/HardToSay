class MyStack(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue = self.queue[1:] + [self.queue[0]]
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue) == 0:
            return 0

        rtn = self.queue[0]
        self.queue = self.queue[1:]
        return rtn
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.queue) == 0:
            return 0
        return self.queue[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print obj.top()
param_2 = obj.pop()
print param_2, obj.empty()
# param_3 = obj.top()
# param_4 = obj.empty()