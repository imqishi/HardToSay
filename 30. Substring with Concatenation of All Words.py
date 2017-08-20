import copy
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if s == "" or len(words) == 0:
            return result
        need = {}
        for word in words:
            need[word] = need[word] + 1 if word in need else 1
        wordLen = len(words[0])
        sLen = len(s)
        wordCount = len(words)
        subLen = wordLen * wordCount
        i = 0
        while i < sLen - subLen + 1:
            tmp = copy.copy(need)
            count = 0
            subCount = i + subLen
            k = i
            while k < subCount:
                ts = s[k : k + wordLen]
                if ts not in tmp:
                    i += 1
                    break
                else:
                    if tmp[ts] > 0:
                        tmp[ts] -= 1
                        k += wordLen
                        count += 1
                    else:
                        i += 1
                        break

                if count == wordCount:
                    result.append(i)
                    tmp = {}
                    i += 1

        return result


obj = Solution()
print obj.findSubstring('adfa', ['a', 'd'])