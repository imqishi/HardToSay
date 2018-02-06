class Heap(object):
    def hsortMax(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n = len(a)
        for i in range(n / 2 - 1, -1, -1):
            self.adjustMax(a, i, n)

        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]
            self.adjustMax(a, 0, i)
    
        return a

    def adjustMax(self, a, i, n):
        child = 0
        tmp = a[i]
        while (i * 2 + 1) < n:
            child = i * 2 + 1
            if child != n - 1 and a[child + 1] > a[child]:
                child += 1
            if tmp < a[child]:
                a[i] = a[child]
            else:
                break
            i = child
        a[i] = tmp

    def hsortMin(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n = len(a)
        for i in range(n / 2 - 1, -1, -1):
            self.adjustMin(a, i, n)

        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]
            self.adjustMin(a, 0, i)
    
        return a

    def adjustMin(self, a, i, n):
        child = 0
        tmp = a[i]
        while (i * 2 + 1) < n:
            child = i * 2 + 1
            if child != n - 1 and a[child + 1] < a[child]:
                child += 1
            if tmp > a[child]:
                a[i] = a[child]
            else:
                break
            i = child
        a[i] = tmp

obj = Heap()
print obj.hsortMax([5,7,6,3,2,8,9,1])
print obj.hsortMax([5,7,6,3])
print obj.hsortMax([5,7,6])
print obj.hsortMax([5,7])
print obj.hsortMax([5])

print obj.hsortMin([5,7,6,3,2,8,9,1])
print obj.hsortMin([5,7,6,3])
print obj.hsortMin([5,7,6])
print obj.hsortMin([5,7])
print obj.hsortMin([5])