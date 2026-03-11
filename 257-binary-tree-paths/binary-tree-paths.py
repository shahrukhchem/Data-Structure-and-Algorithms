# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths=[]
        res=[]
        def dfsrecur(node,res):
            res.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(res))
            if node.left:
                dfsrecur(node.left,res)
            if node.right:
                dfsrecur(node.right,res)
            res.pop()
        dfsrecur(root,res)
        print(paths)
        return paths

        