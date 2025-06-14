from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        zigzag_order = []
        nodes = [root]
        level = 0
        while nodes:
            zigzag_order_in_level = deque([])
            nodes_next_level = []
            for node in nodes:
                if level % 2 == 0:
                    zigzag_order_in_level.append(node.val)
                else:
                    zigzag_order_in_level.appendleft(node.val)
                if node.left is not None:
                    nodes_next_level.append(node.left)
                if node.right is not None:
                    nodes_next_level.append(node.right)
            nodes = nodes_next_level
            zigzag_order.append(list(zigzag_order_in_level))
            level += 1
            
        return zigzag_order





from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_zigzag_order_and_next_level(nodes, level):
            zigzag_order_in_level = deque([])
            nodes_next_level = []
            for node in nodes:
                if level % 2 == 0:
                    zigzag_order_in_level.append(node.val)
                else:
                    zigzag_order_in_level.appendleft(node.val)
                if node.left is not None:
                    nodes_next_level.append(node.left)
                if node.right is not None:
                    nodes_next_level.append(node.right)
            return zigzag_order_in_level, nodes_next_level

        if root is None:
            return []
        zigzag_order = []
        nodes = [root]
        level = 0
        while nodes:
            zigzag_order_in_level, nodes_next_level = get_zigzag_order_and_next_level(nodes, level)
            nodes = nodes_next_level
            zigzag_order.append(list(zigzag_order_in_level))
            level += 1
            
        return zigzag_order
