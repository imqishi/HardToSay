class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = end = res = 0
        minWidth = False
        while end < len(nums):
            while end < len(nums) and res < s:
                res += nums[end]
                end += 1
            
            if res < s:
                break

            while start < end and res >= s:
                res -= nums[start]
                start += 1
            
            if minWidth is False or end - start + 1 < minWidth:
                minWidth = end - start + 1

        return minWidth if minWidth is not False else 0

    def minSubArrayLenNLogN(self, s, nums):
        sums = [0] * (len(nums) + 1)
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + nums[i-1]

        minWidth = False
        for i in range(len(sums)):
            end = self.binarySearch(i + 1, len(sums) - 1, sums[i] + s, sums)
            if end == len(sums):
                break
            if minWidth is False or end - i < minWidth:
                minWidth = end - i

        return minWidth if minWidth is not False else 0

    def binarySearch(self, lo, hi, key, sums):
        while lo <= hi:
           mid = (lo + hi) / 2
           if sums[mid] >= key:
               hi = mid - 1
           else:
               lo = mid + 1
        return lo

obj = Solution()
print obj.minSubArrayLen(5, [1,2,1,3,4,5])
print obj.minSubArrayLenNLogN(5, [1,2,1,3,4,5])