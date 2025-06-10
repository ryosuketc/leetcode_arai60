# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge_sort_helper(left, right):
            if not pairs:
                return []
            if left == right:
                return [pairs[right]]
            middle = (left + right) // 2
            pairs1 = merge_sort_helper(left, middle)
            pairs2 = merge_sort_helper(middle + 1, right)

            merged = []
            index1 = 0
            index2 = 0
            while index1 < len(pairs1) and index2 < len(pairs2):
                if pairs1[index1].key <= pairs2[index2].key:
                    merged.append(pairs1[index1])
                    index1 += 1
                else:
                    merged.append(pairs2[index2])
                    index2 += 1
            if index1 < len(pairs1):
                merged.extend(pairs1[index1:])
            if index2 < len(pairs2):
                merged.extend(pairs2[index2:])
            return merged

        return merge_sort_helper(0, len(pairs) - 1)
