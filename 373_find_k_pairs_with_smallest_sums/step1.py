from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        smallest_pairs = []
        visited = set()
        remaining = k
        # sum, (num1_index, num2_index)
        heap = [(nums1[0] + nums2[0], (0, 0))]

        while remaining > 0 and heap:
            sum_, (nums1_index, nums2_index) = heappop(heap)
            smallest_pairs.append((nums1[nums1_index], nums2[nums2_index]))

            if nums1_index + 1 < len(nums1) and (nums1_index + 1, nums2_index) not in visited:
                heappush(heap, (nums1[nums1_index + 1] + nums2[nums2_index], (nums1_index + 1, nums2_index)))
                visited.add((nums1_index + 1, nums2_index))
            if nums2_index + 1 < len(nums2) and (nums1_index, nums2_index + 1) not in visited:
                heappush(heap, (nums1[nums1_index] + nums2[nums2_index + 1], (nums1_index, nums2_index + 1)))
                visited.add((nums1_index, nums2_index + 1))
            
            remaining -= 1
        
        return smallest_pairs
