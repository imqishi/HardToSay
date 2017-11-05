import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        This function is ERROR!!!
        Still can not understand this...
        """
        beginSet = [beginWord]
        endSet = [endWord]
        wordLen = len(beginWord)
        depth = 2
        while len(beginSet) != 0 and len(endSet) != 0:
            # Every time make beginSet is the small one
            # So we try to get smaller nextSet and make it faster
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            tmp = []
            for word in beginSet:
                for i in range(wordLen):
                    # Try every case
                    for ch in string.ascii_lowercase:
                        if i != wordLen - 1:
                            newWord = word[:i] + ch + word[i+1:]
                        else:
                            newWord = word[:i] + ch
                        if newWord in endSet and newWord != endSet[-1]:
                            print newWord, endSet
                            return depth
                        if newWord in wordList and newWord != wordList[-1]:
                            print newWord
                            tmp.append(newWord)
                            wordList.remove(newWord)
            print 'level'
            depth += 1
            beginSet = tmp
        
        return 0


    def ladderLengthSlow(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wait = self.getNextLevel(beginWord, wordList)
        depth = 2
        while len(wait):
            next_level = []
            for item in wait:
                if item == endWord:
                    return depth
                next_level += self.getNextLevel(item, wordList)
            wait = next_level
            depth += 1

        return 0

    def getNextLevel(self, word, wordList):
        res = []
        if word in wordList:
            wordList.remove(word)
        for (i, x) in enumerate(word):
            for y in string.ascii_lowercase:
                if i < len(word) - 1:
                    tmp = word[:i] + y + word[i+1:]
                else:
                    tmp = word[:i] + y
                if tmp in wordList:
                    res.append(tmp)
                    wordList.remove(tmp)

        return res

obj = Solution()
print obj.ladderLengthSlow('hit', 'cog', ["hot","dot","dog","lot","log"])