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
        level = 0
        nodes_with_level = deque([(root, level)])
        result = []
        while nodes_with_level:
            node, level = nodes_with_level.popleft()
            # Usually executed only once as the tree is traversed by each level.
            while len(result) <= level:
                result.append([])
            result[level].append(node.val)
            if node.left is not None:
                nodes_with_level.append((node.left, level + 1))
            if node.right is not None:
                nodes_with_level.append((node.right, level + 1))
        return result
