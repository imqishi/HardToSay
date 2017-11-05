# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        pre = root
        last_pre = pre
        firstLoop = True
        while pre != last_pre or firstLoop:
            firstLoop = False
            now = pre
            last_pre = pre
            left = None
            while now is not None:
                if now.left is not None:
                    if left is None:
                        left = now.left
                        pre = now.left
                    else:
                        left.next = now.left
                        left = now.left
                if now.right is not None:
                    if left is None:
                        left = now.right
                        pre = now.right
                    else:
                        left.next = now.right
                        left = now.right
                now = now.next

