class Solution1:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth_grammer_helper(n, k, root_val):
            if n == 1:
                return root_val
            total_nodes = 2 ** (n - 1)
            half_of_total_nodes = total_nodes // 2
            # Target node will be in the right half -> reverse
            if k > total_nodes / 2:
                return kth_grammer_helper(n - 1, k - half_of_total_nodes, root_val ^ 1)
            # Target node will be in the left half -> not reverse
            return kth_grammer_helper(n - 1, k, root_val)
        
        return kth_grammer_helper(n, k, 0)


class Solution2:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth_grammer_helper(n, k):
            if n == 1:
                return 0
            total_nodes = 2 ** (n - 1)
            half_of_total_nodes = total_nodes // 2
            # Target node will be in the right half,
            # 1. move to the left half (k - half_of_total_nodes),
            # 2. reverse (1 ^ ...),
            # 3. and go up (n - 1).
            if k > half_of_total_nodes:
                return 1 ^ kth_grammer_helper(n - 1, k - half_of_total_nodes)
            # Target node will be in the left half -> not reverse. Just go up (n - 1)
            return kth_grammer_helper(n - 1, k)
        
        return kth_grammer_helper(n, k)


class Solution3:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k - 1).bit_count() & 1
