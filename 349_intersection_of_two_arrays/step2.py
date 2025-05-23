class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i1 = 0
        i2 = 0
        result = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
                continue
            if nums1[i1] > nums2[i2]:
                i2 += 1
                continue

            common = nums1[i1]
            result.append(common)

            while i1 < len(nums1) and nums1[i1] == common:
                i1 += 1
            while i2 < len(nums2) and nums2[i2] == common:
                i2 += 1

        return result
