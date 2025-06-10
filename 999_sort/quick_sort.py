# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def swap(index1, index2):
            pairs[index1], pairs[index2] = pairs[index2], pairs[index1]

        def partition(left, right):
            if left > right:
                return
            pivot_value = pairs[right].key
            # right position of piviot found so far
            smaller_index = left
            for i in range(left, right):
                if pairs[i].key < pivot_value:
                    swap(smaller_index, i)
                    smaller_index += 1
            # Put the pivot in the right position.
            swap(smaller_index, right)

            partition(left, smaller_index - 1)
            partition(smaller_index + 1, right)

        partition(0, len(pairs) - 1)
        return pairs
