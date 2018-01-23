class Trie(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {
            'isEnd': True,
            'neighbors': {}
        }
        

    def insert(self, word):
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
        ptr = self.root
        for ch in word:
            if ch not in ptr['neighbors']:
                return False
            ptr = ptr['neighbors'][ch]
        
        return ptr['isEnd']
            
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = self.root
        for ch in prefix:
            if ch not in ptr['neighbors']:
                return False
            ptr = ptr['neighbors'][ch]
        
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = 'helloworld'
search = 'word'
prefix = 'hello'
obj.insert(word)
param_2 = obj.search(search)
param_3 = obj.startsWith(prefix)
print param_2, param_3