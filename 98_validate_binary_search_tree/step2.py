from math import inf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            False
        # Stack (node, lower_bound, upper_bound, both exclusive)
        nodes = [(root, -inf, inf)]
        while nodes:
            node, lower_bound, upper_bound = nodes.pop()
            if not (lower_bound < node.val < upper_bound):
                return False
            if node.left is not None:
                nodes.append((node.left, lower_bound, node.val))
            if node.right is not None:
                nodes.append((node.right, node.val, upper_bound))
        return True

