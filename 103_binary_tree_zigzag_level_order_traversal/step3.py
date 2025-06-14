from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        zigzag_order = []
        nodes = [root]
        level = 0
        while nodes:
            zigzag_order_in_level = deque([])
            next_nodes = []
            for node in nodes:
                if level % 2 == 0:
                    zigzag_order_in_level.append(node.val)
                else:
                    zigzag_order_in_level.appendleft(node.val)
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            zigzag_order.append(list(zigzag_order_in_level))
            level += 1
            nodes = next_nodes
        return zigzag_order
