# -*- coding: utf-8 -*-
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= numRows or numRows == 1:
            return s
        rtn = ""
        i = 0
        while i < numRows:
            turn = 0
            j = i
            while j < length:
                rtn += s[j]
                if i == 0 or i == numRows - 1:
                    j += numRows * 2 - 2
                else:
                    if turn == 0:
                        j = j + numRows * 2 - i * 2 - 2
                    else:
                        j = j + i * 2
                    turn = 1 - turn
            i += 1

        return rtn

    def convertSimple(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rtn = {}
        for i in range(numRows):
            rtn[i] = []

        # turn 1 正序 -1 倒序
        turn = -1
        cur = 0
        for (i, c) in enumerate(s):
            if i % (numRows-1) == 0:
                turn = 1 if turn == -1 else -1

            rtn[cur].append(c)
            cur += turn

        str = "";
        for i in range(numRows):
            str += "".join(rtn[i])
        return str

solution = Solution()
print solution.convertSimple("ABCDEFGHIJKLMN", 5)