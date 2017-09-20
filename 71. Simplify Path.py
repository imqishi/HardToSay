class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathArr = path.split('/')
        stack = []
        for i in pathArr:
            if i == '':
                continue
            elif i == '.':
                continue
            elif i == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            return '/'
        else:
            return '/' + '/'.join(stack)

obj = Solution()
print obj.simplifyPath('/../a/b/.././c')