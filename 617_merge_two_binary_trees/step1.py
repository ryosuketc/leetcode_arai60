# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Runtime error
class Solution1:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_trees_helper(node1, node2):
            if node1 is None and node2 is None:
                return None
            node1_val = node1.val if node1 is not None else 0
            node2_val = node2.val if node2 is not None else 0
            new_node = TreeNode(node1_val + node2_val)
            new_node.left = merge_trees_helper(node1.left, node2.left)
            new_node.right = merge_trees_helper(node1.right, node2.right)
            return new_node

        return merge_trees_helper(root1, root2)


# ベタ書き。これはひどい
# Accepted
class Solution2:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_trees_helper(node1, node2):
            if node1 is None and node2 is None:
                return None
            node1_val = node1.val if node1 is not None else 0
            node2_val = node2.val if node2 is not None else 0
            new_node = TreeNode(node1_val + node2_val)
            if node1 is not None and node2 is not None:
                node1_left = node1.left
                node1_right = node1.right
                node2_left = node2.left
                node2_right = node2.right
            elif node1 is None:
                node1_left = None
                node1_right = None
                node2_left = node2.left
                node2_right = node2.right
            elif node2 is None:
                node1_left = node1.left
                node1_right = node1.right
                node2_left = None
                node2_right = None
        
            new_node.left = merge_trees_helper(node1_left, node2_left)
            new_node.right = merge_trees_helper(node1_right, node2_right)
            return new_node

        return merge_trees_helper(root1, root2)
