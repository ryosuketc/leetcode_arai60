# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sorted_array_to_bst_helper(start_index, end_index):
            if end_index < start_index:
                return None
            middle_index = (start_index + end_index) // 2
            root = TreeNode(nums[middle_index])
            root.left = sorted_array_to_bst_helper(start_index, middle_index - 1)
            root.right = sorted_array_to_bst_helper(middle_index + 1, end_index)
            return root
        
        return sorted_array_to_bst_helper(0, len(nums) - 1)
