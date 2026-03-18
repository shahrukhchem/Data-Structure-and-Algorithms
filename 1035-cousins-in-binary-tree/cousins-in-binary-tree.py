# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        tree=deque([(root,1,None)])
        res={}
        xyparent=[]
        xylevel=[]
        while tree:
            node,level,parent=tree.popleft()
            if node.val==x or node.val==y:
                    xylevel.append(level)
                    xyparent.append(parent)
            if node.left:
                tree.append((node.left,level+1,node.val))
            if node.right:
                tree.append((node.right,level+1,node.val))
        if len(set(xylevel))==1 and len(set(xyparent))==2:
            return True
        return False
        
        