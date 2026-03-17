# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        tree=deque()
        tree.append(root)
        sum=0
        while tree:
            
            if tree[0].left:
                tree.append(tree[0].left)
                if not tree[0].left.left and not tree[0].left.right :
                    sum=sum+tree[0].left.val
            if tree[0].right:
                tree.append(tree[0].right)
            tree.popleft()
        return sum