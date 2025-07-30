class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))

        return max_depth
