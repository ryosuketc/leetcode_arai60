from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def add_smallest_candidates(nums1_index, nums2_index) -> None:
            key = (nums1_index, nums2_index)
            if key in visited:
                return
            visited.add(key)
            total = nums1[nums1_index] + nums2[nums2_index]
            heappush(smallest_candidates, (total, key))


        smallest_pairs = []
        visited = set()
        remaining = k
        # Min heap of sum, (num1_index, num2_index).
        # The first numbers are guranteed to be the smalleset since the lists are in non decreasing order.
        smallest_candidates = [(nums1[0] + nums2[0], (0, 0))]

        while remaining > 0 and smallest_candidates:
            _, (nums1_index, nums2_index) = heappop(smallest_candidates)
            smallest_pairs.append([nums1[nums1_index], nums2[nums2_index]])

            if nums1_index + 1 < len(nums1):
                add_smallest_candidates(nums1_index + 1, nums2_index)
            if nums2_index + 1 < len(nums2):
                add_smallest_candidates(nums1_index, nums2_index + 1)
            
            remaining -= 1
        return smallest_pairs


from heapq import heappop, heappush


class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def add_smallest_candidates(nums1_index, nums2_index) -> None:
            if nums1_index >= len(nums1) or nums2_index >= len(nums2):
                return
            key = (nums1_index, nums2_index)
            if key in visited:
                return
            visited.add(key)
            total = nums1[nums1_index] + nums2[nums2_index]
            heappush(smallest_candidates, (total, key))


        smallest_pairs = []
        visited = set()
        remaining = k
        # Min heap of sum, (num1_index, num2_index)
        # The first numbers are guranteed to be the smalleset since the lists are in non decreasing order.
        smallest_candidates = [(nums1[0] + nums2[0], (0, 0))]

        while remaining > 0 and smallest_candidates:
            _, (nums1_index, nums2_index) = heappop(smallest_candidates)
            smallest_pairs.append([nums1[nums1_index], nums2[nums2_index]])

            add_smallest_candidates(nums1_index + 1, nums2_index)
            add_smallest_candidates(nums1_index, nums2_index + 1)
            
            remaining -= 1
        return smallest_pairs
