from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        current_level = [root]
        next_level = []
        while current_level:
            nodes_in_this_level = []
            for node in current_level:
                nodes_in_this_level.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            result.append(nodes_in_this_level)
            current_level = next_level
            next_level = []
        
        return result
