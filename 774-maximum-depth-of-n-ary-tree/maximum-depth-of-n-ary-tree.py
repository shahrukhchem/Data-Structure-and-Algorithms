"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        tree=deque([(root,1)])
        while tree:
            node,level=tree.popleft()
            for child in node.children:
                tree.append((child,level+1))
        return level
        