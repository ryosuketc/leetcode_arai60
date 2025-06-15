# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if root is None:
            return None, None
        elif root.val <= target:
            bns = self.splitBST(root.right, target)
            root.right = bns[0]
            return root, bns[1]
        else:
            bns = self.splitBST(root.left, target)
            root.left = bns[1]
            return bns[0], root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        dummy_smaller = TreeNode()
        dummy_larger = TreeNode()
        node_smaller = dummy_smaller
        node_larger = dummy_larger

        node = root
        next_node = None

        while node is not None:
            if node.val <= target:
                node_smaller.right = node
                node_smaller = node
                next_node = node.right
                node.right = None
                node = next_node
            else:
                node_larger.left = node
                node_larger = node
                next_node = node.left
                node.left = None
                node = next_node
        
        return [dummy_smaller.right, dummy_larger.left]
