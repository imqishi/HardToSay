class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        sub_res = [1]
        if rowIndex == 0:
            return sub_res
        sub_res = [1, 1]
        if rowIndex == 1:
            return sub_res
        for x in range(2, rowIndex + 1):
            tmp = []
            for i, y in enumerate(sub_res):
                if i == 0:
                    tmp.append(y)
                    tmp.append(y + sub_res[1])
                elif i == len(sub_res) - 1:
                    tmp.append(1)
                else:
                    tmp.append(sub_res[i] + sub_res[i+1])
            sub_res = tmp

        return sub_res

obj = Solution()
print obj.getRow(3)