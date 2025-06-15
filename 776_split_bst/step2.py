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
        if root.val <= target:
            # No need to edit root and root.left -> recurse on root.right.
            smaller, larger = self.splitBST(root.right, target)
            # root belongs to the left subtree. So smaller should be placed under root.
            root.right = smaller
            return root, larger
        else:
            smaller, larger = self.splitBST(root.left, target)
            root.left = larger
            return smaller, root

# Iterative -> from LeetCode approach 2
class Solution2:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:

        # List to store the two split trees
        ans = [None, None]

        # If root is None, return the empty list
        if not root:
            return ans
        # Stack to traverse the tree and find the split point
        stack = []
        # Find the node with the value closest to the target
        while root:
            stack.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right
        # Process nodes in reverse order from the stack to perform the split
        while stack:
            curr = stack.pop()
            if curr.val > target:
                # Assign current node's left child to the subtree
                # containing nodes greater than the target
                curr.left = ans[1]
                # current node becomes the new root of this subtree
                ans[1] = curr
            else:
                # Assign current node's right child to the subtree
                # containing nodes smaller than the target
                curr.right = ans[0]
                # current node becomes the new root of this subtree
                ans[0] = curr
        return ans
