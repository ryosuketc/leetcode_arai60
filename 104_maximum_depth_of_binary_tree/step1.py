class SolutionRuntimeError:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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


class SolutionAC:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            max_depth = max(max_depth, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

        return max_depth
