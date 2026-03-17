# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        tree=deque()
        tree.append(root)
        res=[]
        while tree:
            print(tree[0].val)
            if tree[0].right:
                tree.append(tree[0].right)
            if tree[0].left:
                tree.append(tree[0].left)
            x=tree.popleft()
            res.append(x.val)
        return res[-1]


        
        