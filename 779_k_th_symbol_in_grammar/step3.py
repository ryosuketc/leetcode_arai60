class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth_grammer_helper(n, k):
            if n == 1:
                return 0
            total_nodes = 2 ** (n - 1)
            half_of_total_nodes = total_nodes // 2
            # Target node will be in the right half -> flip,
            if k > half_of_total_nodes:
                return 1 ^ kth_grammer_helper(n - 1, k - half_of_total_nodes)
            # Target node will be in the left half -> not flip.
            return kth_grammer_helper(n - 1, k)
        
        return kth_grammer_helper(n, k)
