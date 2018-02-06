class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        t = []
        while len(self.stack) != 0:
            t.append(self.stack.pop())
        rtn = t.pop()
        while len(t) != 0:
            self.stack.append(t.pop())
        return rtn

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        t = []
        while len(self.stack) != 0:
            t.append(self.stack.pop())
        rtn = t.pop()
        self.stack.append(rtn)
        while len(t) != 0:
            self.stack.append(t.pop())
        
        return rtn
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print obj.peek()
#param_2 = obj.pop()
#param_3 = obj.peek()
#param_4 = obj.empty()