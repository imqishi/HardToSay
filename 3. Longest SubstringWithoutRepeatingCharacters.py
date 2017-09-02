# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #初步思路
        #利用一个dict结构判断是否出现重复字母
        #利用一个rtn作为当前最优串
        #利用一个t_string作为当前进行查找的串
        #开始遍历：
        #    如果出现重复字母，
        #        比较当前进行串和最优串谁最长，若进行串更长，则替换最优串
        #        找出重复的字母在进行串中的位置，从该位置截取获得接下来继续进行遍历的串并对dict进行清理。如果就是最后一个，那么直接将进行串及dict置空
        #    把当前的字母分别存到t_string和dict里面
        #结束遍历：
        #    如果t_string比rtn长，则将rtn置为t_string
        rtn = ''
        t_string = ''
        dict = {}
        for c in s:
            if dict.has_key(c):
                if(len(rtn) < len(t_string)):
                    rtn = t_string
                pos = t_string.find(c)
                if len(t_string) > pos + 1:
                    for tc in t_string[:pos+1]:
                        del dict[tc]
                    t_string = t_string[pos+1:]
                else:
                    dict = {}
                    t_string = ''
            dict[c] = 1
            t_string += c

        if (not rtn) or (len(rtn) < len(t_string)):
            rtn = t_string
        return len(rtn)



obj = Solution();
print obj.lengthOfLongestSubstring('deabcfadegh')