from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_strs = defaultdict(list)
        for s in strs:
            sorted_key = tuple(sorted(s))
            sorted_str_to_strs[sorted_key].append(s)

        return list(sorted_str_to_strs.values())
