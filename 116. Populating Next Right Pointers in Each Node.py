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
        while pre.left is not None:
            now = pre
            while now is not None:
                now.left.next = now.right
                if now.next is not None:
                    now.right.next = now.next.left
                now = now.next

            pre = pre.left


    def connectUseExtraSpace(self, root):
        if root is None:
            return
        sub_res = [root]
        while len(sub_res) != 0:
            tmp = []
            for x in sub_res:
                if x.left is not None:
                    tmp.append(x.left)
                if x.right is not None:
                    tmp.append(x.right)
            for i, x in enumerate(tmp):
                if i + 1 >= len(tmp):
                    x.next = None
                else:
                    tmp[i].next = tmp[i+1]
            sub_res = tmp[:]

