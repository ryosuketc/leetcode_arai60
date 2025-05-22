from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_original = defaultdict(list)
        for s in strs:
            sorted_str = tuple(sorted(s))
            sorted_str_to_original[sorted_str].append(s)
        return list(sorted_str_to_original.values())
    

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_original = defaultdict(list)
        for s in strs:
            sorted_str_key = tuple(sorted(s))
            sorted_str_to_original[sorted_str_key].append(s)
        return list(sorted_str_to_original.values())


class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_original = defaultdict(list)
        for s in strs:
            sorted_str_key = tuple(sorted(s))
            sorted_str_to_original[sorted_str_key].append(s)
        return list(sorted_str_to_original.values())
