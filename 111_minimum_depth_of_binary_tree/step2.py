from math import inf, isinf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        min_depth = inf

        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
                continue
            for child in (node.left, node.right):
                stack.append((child, depth + 1))
        
        if isinf(min_depth):
            min_depth = 0
        return min_depth


from math import inf, isinf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRuntimeError:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = math.inf
        nodes_with_depth = [(root, 1)]

        while nodes_with_depth:
            node, depth = nodes_with_depth.pop()
            if node is None:
                continue
            children = (node.left, node.right)
            if all(children, lambda x: x is None):
                min_depth = min(min_depth, depth)
                continue
            for child in children:
                nodes_with_depth.append((child, depth + 1))
        
        if isinf(min_depth):
            return 0
        return min_depth
