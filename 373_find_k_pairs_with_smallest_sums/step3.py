from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def add_smallest_candidate(nums1_index, nums2_index) -> None:
            key = (nums1_index, nums2_index)
            if nums1_index >= len(nums1) or nums2_index >= len(nums2) or key in visited:
                return
            visited.add(key)
            total = nums1[nums1_index] + nums2[nums2_index]
            heappush(smallest_pair_candidates, (total, key))


        smallest_pairs = []
        num_pairs_found = 0
        visited = set()
        smallest_pair_candidates = [(nums1[0] + nums2[0], (0, 0))]

        while num_pairs_found < k and smallest_pair_candidates:
            _, (nums1_index, nums2_index) = heappop(smallest_pair_candidates)
            smallest_pairs.append([nums1[nums1_index], nums2[nums2_index]])
            add_smallest_candidate(nums1_index + 1, nums2_index)
            add_smallest_candidate(nums1_index, nums2_index + 1)

            num_pairs_found += 1

        return smallest_pairs
