# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        middle_index = len(nums) // 2
        root = TreeNode(nums[middle_index])
        root.left = self.sortedArrayToBST(nums[:middle_index])
        root.right = self.sortedArrayToBST(nums[middle_index + 1:])
        return root

