class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        max: 2147483647
        min: -2147483648
        """
        max = "2147483647"
        max_num = 2147483647
        type = True
        s = s.strip()
        length = len(s)
        if length < 1:
            return 0

        if s[0] == '-':
            type = not type
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for (i, c) in enumerate(s):
            try:
                t = int(c)
            except:
                s = s[:i]

        if len(s) > 10:
            return max_num if type else - max_num -1

        num = 0
        for (i, c) in enumerate(s):
            try:
                c_int = int(c)
            except:
                return num if type else -num
            if i == 9:
                same = True
                for (j, t) in enumerate(str(num)):
                    if t != max[j]:
                        same = False
                    if same and t > max[j]:
                        return max_num if type else -max_num-1

                if same and type and c_int > 7:
                    return max_num
                elif same and not type and c_int > 8:
                    return -max_num-1

            num = num * 10 + c_int

        return num if type else -num

obj = Solution()
print obj.myAtoi("1095502006")
print obj.myAtoi("-2147483649")
print obj.myAtoi("2147483648")
print obj.myAtoi("1192820738r2")
print obj.myAtoi("214748364689")
print obj.myAtoi("-1010023630o4")
print obj.myAtoi("-2147483649")
print obj.myAtoi("   -1123u3761867")
print obj.myAtoi("   -1123")
print obj.myAtoi("   1123u3761867")
print obj.myAtoi("   +=")
print obj.myAtoi("-2147483648")
print obj.myAtoi("2147483647")
print obj.myAtoi("112147483647")
