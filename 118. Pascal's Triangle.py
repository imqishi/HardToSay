class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        sub_res = [1]
        res = []
        res.append(sub_res[:])
        if numRows == 1:
            return res
        sub_res = [1, 1]
        res.append(sub_res[:])
        if numRows == 2:
            return res
        for x in range(3, numRows + 1):
            tmp = []
            for i, y in enumerate(sub_res):
                if i == 0:
                    tmp.append(y)
                    tmp.append(y + sub_res[1])
                elif i == len(sub_res) - 1:
                    tmp.append(1)
                else:
                    tmp.append(sub_res[i] + sub_res[i+1])
            res.append(tmp[:])
            sub_res = tmp

        return res

obj = Solution()
obj.generate(4)
