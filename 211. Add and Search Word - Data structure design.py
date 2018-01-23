class WordDictionary(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {
            'isEnd': True,
            'neighbors': {}
        }
        

    def addWord(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for ch in word:
            if ch in ptr['neighbors']:
                ptr = ptr['neighbors'][ch]
            else:
                ptr['neighbors'][ch] = {
                    'isEnd': False,
                    'neighbors': {}
                }
                ptr = ptr['neighbors'][ch]
        ptr['isEnd'] = True
        return
            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.subSearch(word, self.root)

    def subSearch(self, word, ptr):
        res = False
        for (i, ch) in enumerate(word):
            if ch != '.':
                if ch not in ptr['neighbors']:
                    return False
                else:
                    ptr = ptr['neighbors'][ch]
            else:
                for t in ptr['neighbors']:
                    if self.subSearch(word[i+1:], ptr['neighbors'][t]):
                        return True
                return False

        return ptr['isEnd']


obj = WordDictionary()
word = 'helloworld'
search = 'h...world'
obj.addWord('a')
obj.addWord('a')
param_2 = obj.search('.a')
print param_2