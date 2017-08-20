class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 2:
            return 0
        max = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if j > i:
                    if height[i] == 0 or height[j] == 0:
                        continue
                    h = height[i] if height[i] < height[j] else height[j]
                    t = (j - i) * h
                    max = t if max < t else max

        return max

    def maxAreaN(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Max = 0
        i = 0
        j = len(height) - 1
        while i != j:
            tm = (j - i) * min(height[i], height[j])
            Max = tm if tm > Max else Max
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return Max

obj = Solution()
print obj.maxAreaN([1, 2, 4, 3])