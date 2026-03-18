# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        tree=deque([root])
        values=[]
        while tree:
            values.append(tree[0].val)
            if tree[0].left:
                tree.append(tree[0].left)
            if tree[0].right:
                tree.append(tree[0].right)
            tree.popleft()
        if len(set(values))>1:
            return False
        else:
            return True