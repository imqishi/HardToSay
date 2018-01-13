class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s) + 1)]
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i:i+len(word)]:
                    if i == 0:
                        dp[i] = dp[i+len(word)] = True
                    else:
                        if dp[i] is True:
                            dp[i+len(word)] = True
        return dp[len(s)]
                

    def wordBreakForce(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        realDict = {}
        for word in wordDict:
            if word[0] not in realDict:
                realDict[word[0]] = [word]
            else:
                realDict[word[0]].append(word)
        
        i = 0
        length = len(s)
        if s[i] not in realDict:
            return False

        # init
        res = []
        for word in realDict[s[i]]:
            if word == s[:len(word)]:
                res.append(len(word))

        while len(res) > 0:
            bak_res = []
            for next_start in res:
                if next_start == len(s):
                    return True
                if s[next_start] not in realDict:
                    continue
                else:
                    for word in realDict[s[next_start]]:
                        if word == s[next_start:next_start + len(word)]:
                            bak_res.append(next_start + len(word))
            res = bak_res
        
        return False

obj = Solution()
print obj.wordBreak('leetcode', ["leet","code"])