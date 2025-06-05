from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

_RIGHT_TO_LEFT = "RIGHT_TO_LEFT"
_LEFT_TO_RIGHT = "LEFT_TO_RIGHT"

# Wrong Answer
class Solution1:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_direction(level):
            if level % 2 == 0:
                return _LEFT_TO_RIGHT
            return _RIGHT_TO_LEFT

        if root is None:
            return []
        level = 0
        nodes_with_level = deque([(root, level)])
        result = []
        while nodes_with_level:
            node, level = nodes_with_level.popleft()
            while len(result) <= level:
                result.append([])
            result[level].append(node.val)

            if get_direction(level + 1) == _LEFT_TO_RIGHT:
                if node.left is not None:
                    nodes_with_level.append((node.left, level + 1))
                if node.right is not None:
                    nodes_with_level.append((node.right, level + 1))
            else:
                if node.right is not None:
                    nodes_with_level.append((node.right, level + 1))
                if node.left is not None:
                    nodes_with_level.append((node.left, level + 1))
        
        return result

# Accepted
class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        current_level = [root]
        next_level = []
        going_right = True
        while current_level:
            nodes_in_this_level = []
            for node in current_level:
                nodes_in_this_level.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            if not going_right:
                nodes_in_this_level.reverse()
            result.append(nodes_in_this_level)
            current_level = next_level
            next_level = []
            going_right = not going_right 

        return result
