class Solution(object):
    def mergeInPosition(self, nums1, m , nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n] 

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        This solution is Wrong!!!
        Because if you use : operator in a list, it will create a copy not use source data
        """
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        i = j = 0
        while i < len(nums1) and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1 = nums1[:i] + [nums2[j]] + nums1[i:]
                i += 1
                j += 1
        
        if i == len(nums1):
            nums1 = nums1 + nums2[j:]
        
        print nums1

obj = Solution()
obj.merge([0], 0, [1], 1)