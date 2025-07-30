# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        nodes_and_sum_so_far = [(root, 0)]
        while nodes_and_sum_so_far:
            node, sum_so_far = nodes_and_sum_so_far.pop()
            if node is None:
                continue
            path_sum = sum_so_far + node.val
            if node.left is None and node.right is None:
                if path_sum == targetSum:
                    return True
            nodes_and_sum_so_far.append((node.left, path_sum))
            nodes_and_sum_so_far.append((node.right, path_sum))
        return False
