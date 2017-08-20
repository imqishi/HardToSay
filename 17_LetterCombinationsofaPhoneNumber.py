class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_map = {
            '0': ['0'],
            '1': ['1'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        last_result = []
        dlen = len(digits)
        if dlen == 0:
            return []
        last_result = num_map[digits[0]]
        i = 1
        while i < len(digits):
            result = []
            now = num_map[digits[i]]
            for item in last_result:
                for ch in now:
                    result.append(item + ch)

            last_result = result
            i += 1

        return last_result


obj = Solution()
print obj.letterCombinations('3')