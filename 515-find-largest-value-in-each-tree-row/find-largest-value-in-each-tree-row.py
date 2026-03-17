# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
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
            fres.append(max(res[i]))
        return fres
        '''

        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)
            level_max = float('-inf')
            
            for _ in range(level_size):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_max)
        
        return result


        