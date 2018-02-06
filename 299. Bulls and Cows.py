class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        mapper = {}
        for i in secret:
            if i not in mapper:
                mapper[i] = 1
            else:
                mapper[i] += 1
        
        A = 0
        B = 0
        for (index, ch) in enumerate(guess):
            if index < len(secret) and ch == secret[index]:
                A += 1
            if ch in mapper and mapper[ch] >= 1:
                B += 1
                mapper[ch] -= 1

        return str(A) + 'A' + str(B - A) + 'B'
    
    def getHintByOneLoop(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = B = 0
        nums = [0] * 10

        for (index, ch) in enumerate(secret):
            if ch == guess[index]:
                A += 1
            else:
                if nums[int(ch)] < 0:
                    B += 1
                if nums[int(guess[index])] > 0:
                    B += 1
                nums[int(ch)] += 1
                nums[int(guess[index])] -= 1

        return str(A) + 'A' + str(B) + 'B'

obj = Solution()
print obj.getHint('1807', '7810')
print obj.getHint('1123', '0111')