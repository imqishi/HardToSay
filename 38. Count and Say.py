class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        i = 2
        while i <= n:
            j = 0
            output = ''
            while j < len(string):
                ch = string[j]
                count = 1
                while j + 1 < len(string) and string[j] == string[j+1]:
                    j += 1
                    count += 1

                j += 1
                output += str(count) + ch

            string = output
            i += 1

        return string

obj = Solution()
obj.countAndSay(1)
