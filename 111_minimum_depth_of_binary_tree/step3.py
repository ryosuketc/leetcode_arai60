from math import inf, isinf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = inf
        nodes_with_depth = [(root, 1)]

        while nodes_with_depth:
            node, depth = nodes_with_depth.pop()
            if node is None:
                continue
            children = (node.left, node.right)
            if not any(children):
                min_depth = min(min_depth, depth)
                continue
            
            for child in children:
                nodes_with_depth.append((child, depth + 1))
        
        if isinf(min_depth):
            return 0
        return min_depth
