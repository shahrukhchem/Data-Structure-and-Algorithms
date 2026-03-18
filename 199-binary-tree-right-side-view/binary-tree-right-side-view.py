# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        tree=deque([(root,1)])
        res={}
        while tree:
            node,level=tree.popleft()
            if level in res:
                res[level].append(node.val)
            else:
                res[level]=[node.val]
            if node.left:
                tree.append((node.left,level+1))
            if node.right:
                tree.append((node.right,level+1))
        fres=[]
        for i in res:
            fres.append(res[i][-1])
        return fres