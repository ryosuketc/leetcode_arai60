# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree_helper(inorder_left_index, inorder_right_index):
            nonlocal preorder_index
            if inorder_left_index > inorder_right_index:
                return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            inorder_root_index = inorder_value_to_index[root_value]
            preorder_index += 1
            root.left = build_tree_helper(inorder_left_index, inorder_root_index - 1)
            root.right = build_tree_helper(inorder_root_index + 1, inorder_right_index)
            return root

        preorder_index = 0
        inorder_value_to_index = {}
        for i, value in enumerate(inorder):
            inorder_value_to_index[value] = i
        return build_tree_helper(0, len(inorder) - 1)
