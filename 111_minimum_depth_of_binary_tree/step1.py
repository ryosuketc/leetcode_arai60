# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionWA:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        min_depth = float('inf')

        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            min_depth = min(min_depth, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
        
        return min_depth if min_depth != float('inf') else 0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        min_depth = float('inf')

        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
                continue
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
        
        return min_depth if min_depth != float('inf') else 0
