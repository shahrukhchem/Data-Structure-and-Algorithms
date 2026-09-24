# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        stack=[(root,None)]
        strnum=[]
        visited=set()
        parent_map = {}
        while stack:
            currnode,parent=stack.pop()
            if currnode in visited:
                continue
            visited.add(currnode)
            parent_map[currnode] = parent
            if currnode.left==None and currnode.right==None:
                strnums=''
                currparent=currnode
                while currparent is not None:
                    strnums=str(currparent.val)+strnums
                    currparent=parent_map[currparent]
                strnum.append(strnums)
            if currnode.left:
                stack.append((currnode.left,currnode))
            if currnode.right:
                stack.append((currnode.right,currnode))
        ts=0
        for i in strnum:
            ts=ts+int(i)
        return ts
            
        