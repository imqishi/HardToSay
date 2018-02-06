class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left = 0
        clen = len(citations)
        right = clen - 1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] == clen - mid:
                return citations[mid]
            elif citations[mid] > clen - mid:
                right = mid - 1
            else:
                left = mid + 1
        
        return clen - (right + 1)