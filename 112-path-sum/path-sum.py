# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfsrecur(node,sum):
            if not node.right  and not node.left:
                sum=sum+node.val
                if sum==targetSum:
                    return True
                else:
                    return False
            sum=sum+node.val
            if node.left and  dfsrecur(node.left,sum):
                    return True
            if node.right and dfsrecur(node.right,sum):
                    return True
            return False
        sum=0
        return dfsrecur(root,0)