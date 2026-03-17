# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        tree=deque([root])
        while tree:
            if tree[0].right:
                tree.append(tree[0].right)
            if tree[0].left:
                tree.append(tree[0].left)
            x=tree.popleft()
            res=x.val
        return res


        
        