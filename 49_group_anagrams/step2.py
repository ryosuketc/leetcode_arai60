from collections import defaultdict

# 1. 継承するパターン
class MyDefaultDict(dict):
    def __init__(self, default_factory):
        super().__init__()
        self._default_factory = default_factory

    def __getitem__(self, k):
        if k not in self:
            self[k] = self._default_factory()
        return super().__getitem__(k)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_strs = MyDefaultDict(list)
        for s in strs:
            sorted_key = tuple(sorted(s))
            sorted_str_to_strs[sorted_key].append(s)

        return list(sorted_str_to_strs.values())



# インスタンス変数で持つ
class MyDefaultDict2:
    def __init__(self, dict_without_default, default_factory):
        self._dict = dict_without_default
        self._default_factory = default_factory

    def get_item(self, key):
        if key not in self._dict:
            self._dict[key] = self._default_factory()
        return self._dict[key]

    def get_values(self):
        return self._dict.values()


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_strs = MyDefaultDict2({}, list)
        for s in strs:
            sorted_key = tuple(sorted(s))
            sorted_str_to_strs.get_item(sorted_key).append(s)

        return list(sorted_str_to_strs.get_values())
