# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree_helper(inorder_left_index, inorder_right_index):
            if inorder_left_index > inorder_right_index:
                return None
            nonlocal preorder_index

            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            mid = value_to_inorder_index[root.val]
            root.left = build_tree_helper(inorder_left_index, mid - 1)
            root.right = build_tree_helper(mid + 1, inorder_right_index)
            return root
        
        preorder_index = 0
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        value_to_inorder_index = {}
        for i, value in enumerate(inorder):
            value_to_inorder_index[value] = i

        return build_tree_helper(0, len(preorder) - 1)
