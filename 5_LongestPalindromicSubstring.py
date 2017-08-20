# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "#" + "#".join(s) + "#"
        RL = {}
        maxRight = 0
        pos = 0
        length = len(s)
        for (i, c) in enumerate(s):
            if i >= maxRight:
                k = 1
                while i - k >= 0 and i + k < length:
                    if s[i-k] != s[i+k]:
                        break
                    k += 1
                RL[i] = k - 1
                maxRight = i + k - 1
                pos = i

            else:
                j = pos * 2 - i
                if RL[j] <= (maxRight - i):
                    k = RL[j] + 1
                    while i - k >= 0 and i + k < length:
                        if s[i-k] != s[i+k]:
                            break
                        k += 1
                    RL[i] = k - 1
                else:
                    k = maxRight - i
                    while i - k >= 0 and i + k < length:
                        if s[i-k] != s[i+k]:
                            break
                        k += 1
                    RL[i] = k - 1

        maxPos = 0
        maxLen = 0
        for i in RL:
            if maxLen < RL[i]:
                maxLen = RL[i]
                maxPos = i

        return s[maxPos - RL[maxPos]:maxPos + RL[maxPos]].replace("#", "")

    def longestPalindrome_dp(self, s):
        length = len(s)
        if length == 1:
            return s
        f = [[0 for i in range(length)] for i in range(length)]
        f[0][0] = 1
        i = 1
        while i < length:
            f[i][i] = 1
            f[i][i - 1] = 1
            i += 1

        maxLeft = maxRight = 0
        k = 2
        while k <= length:
            i = 0
            while i <= length - k:
                if s[i] == s[i+k-1] and f[i+1][i+k-2] == 1:
                    f[i][i+k-1] = 1
                    if maxRight - maxLeft + 1 < k:
                        maxLeft = i
                        maxRight = i + k - 1
                i += 1
            k += 1

        return s[maxLeft:maxRight+1]

    def longestPalindrome_normal(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 0
        max_str = ""
        search_str = ""
        for i in s:
            if i in search_str:
                indices = findIndex(search_str, i)
                #check palindrome
                for index in indices:
                    if len(search_str) == index + 1:
                        if max < 2:
                            max = 2
                            max_str = search_str[index:] + i
                        continue
                    wait_checked = search_str[index:] + i
                    rtn = checkPalindrome(wait_checked)
                    if rtn is False:
                        continue
                    else:
                        if rtn > max:
                            max = rtn
                            max_str = search_str[index:] + i
                        break

            search_str += i

        if max == 0:
            max_str = s[0]
        return max_str

def findIndex(str, needle):
    return [i for i, letter in enumerate(str) if letter == needle]

def checkPalindrome(str):
    check_len = len(str)
    if check_len == 1:
        return 1
    half_len = check_len / 2
    for index, val in enumerate(str):
        if index == half_len:
            break
        count_part = 0 - index - 1;
        if val != str[count_part]:
            return False

    return check_len


obj = Solution()
print obj.longestPalindrome_dp("ccc")
