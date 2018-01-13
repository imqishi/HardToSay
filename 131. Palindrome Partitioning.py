import copy
class Solution(object):
    def partitionByDP(self, s):
        # Init subres[i][j] which means from i to j is Palindrome
        # Obviously, when i == j subres is True
        subres = []
        for i in range(len(s)):
            subres.append([])
            for j in range(len(s)):
                if i == j:
                    subres[i].append(True)
                else:
                    subres[i].append(False)
        result = []
        for i in range(len(s) + 1):
            result.append([])
        result[0].append([])
        for i in range(len(s)):
            result[i+1] = []
            for left in range(i + 1):
                if s[left] == s[i] and (i - left <= 1 or subres[left+1][i-1]):
                    subres[left][i] = True
                    ss = s[left:i+1]
                    for items in result[left]:
                        tmp = copy.copy(items)
                        tmp.append(ss)
                        result[i+1].append(tmp)
        
        return result[len(s)]


    def partitionByBacktrace(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.curList = []
        self.result = []
        self.backtrace(s, 0)
        return self.result
        
    def backtrace(self, s, i):
        if len(self.curList) > 0 and i >= len(s):
            self.result.append(copy.copy(self.curList))
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                self.curList.append(s[i:j + 1])
                self.backtrace(s, j + 1)
                self.curList = self.curList[:-1]
        
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

obj = Solution()
print obj.partitionByDP('aab')