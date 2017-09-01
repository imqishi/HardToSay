class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pos1 = len(num1) - 1
        pos2 = len(num2) - 1
        if pos1 < 0 or pos2 < 0 or num1 == '0' or num2 == '0':
            return '0'
        sub_result = []
        loop = 0
        while pos1 >= 0:
            tmp = []
            j = pos2
            extra = 0
            while j >= 0:
                product = int(num1[pos1]) * int(num2[j]) + extra
                extra = product / 10
                tmp.append(product % 10)
                j -= 1
            if extra != 0:
                tmp.append(extra)
            sub_result.append([0] * loop + tmp)

            loop += 1
            pos1 -= 1
        
        end = len(sub_result) - 1
        max_len = len(sub_result[end])
        i = 0
        extra = 0
        result = []
        while i < max_len:
            j = 0
            tmp = 0  
            while j <= end:
                if i < len(sub_result[j]):
                    tmp += sub_result[j][i]
                j += 1
            
            tmp += extra
            result.append(tmp % 10)
            extra = tmp / 10
            i += 1
        
        if extra != 0:
            result.append(extra)
        result.reverse()
        return ''.join(str(e) for e in result)
            


obj = Solution()
print obj.multiply('1', '0')