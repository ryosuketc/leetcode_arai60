# 392. Is Subsequence

https://leetcode.com/problems/is-subsequence/

## Comments

### step1

*   t の char を consume していって、s の最後まで到達できれば ok というのはすぐに考えた
*   Counter みたいな解法 (anagram 的な) も一瞬考えてみたけど subsequence で、出現回数だけでなく順番も大事だから解けないと思った。
*   4:00 くらいで `SolutionWA` 書いた。
    *   脳内で走らせてみて動くと思ったので submit したが WA。s が空文字列のときを考えていなかった。
    *   `not s` の処理も追加。`not t` が必要なのか考えたけど、`if len(t) < len(s):` でカバーされるはずと考えて追加しなかった。
    *   `not s` の処理をすぐ追加して AC (`SolutionAC`)
*   時間余ったので、follow up についても考えてみたが、よい解法は思いつかなかった。
    *   > Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
    *   今回の解法では t を毎回全部走査しているけど、イメージとしては regex の compile みたいに、t からの情報をを前処理して持っておいて、s が来るたびに、s だけ走査すればよいようにしたい。
    *   `char_to_indidces` みたいな辞書を持っておいて…と考えたが、複数回出現したときの処理が煩雑。indicies を set もしくは list で持つとか考えたけど…動かないけど以下のようなイメージ。
        *   当該の index があるかを探すので set でいいかと思ったが、順番などの処理がうまくいかないのでリストにしてみた。方向性は悪くない気がするが、時間がかかりすぎたので WA な解答として残しておく。
        *   `SolutionWA2` だと、辞書のコピーを作っているので、結局時間計算量 O(len(t)) では、などの問題がある。

```python
from collections import defaultdict


class SolutionWA1:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(t) < len(s):
            return False
        char_to_indices = defaultdict(set)
        for t_index, t_char in enumerate(t):
            char_to_indices[t_char].add(t_index)
        for s_char in s:
            # This condition is not sufficient - what if duplicated chars are in s?
            # e.g. s = "ss", t = "sab" -> char_to_indices = {s: {1}, a: {2}, b: {2}}
            if s_char not in char_to_indices:
                return False
        return True
```

```python
from collections import defaultdict, deque
from copy import deepcopy

class SolutionWA2:
    def preprocess(self, t) -> None: 
        char_to_indices = defaultdict(deque)
        for t_index, t_char in enumerate(t):
            char_to_indices[t_char].append(t_index)
        # This serves as a backup and thus this itself should never be modified.
        self.char_to_indices = char_to_indices

    def isSubsequence(self, s: str, t: str) -> bool:
        self.preprocess(t)
        if not s:
            return True
        if len(t) < len(s):
            return False
        char_to_indices = deepcopy(self.char_to_indices)
        for s_index, s_char in enumerate(s):
            if s_char not in char_to_indices:
                return False
            if not char_to_indices[s_char]:
                return False
            char_to_indices[s_char].popleft()
        return True
```

### step2

*   LeetCode の解答見てみたがごちゃごちゃしていたので中断して他の人の PR 見ることにした。
*   https://github.com/hayashi-ay/leetcode/pull/64/files
    *   自分でも書いてみたがこの書き方きれい `Solution1`
*   https://github.com/olsen-blue/Arai60/pull/58/files
    *   再帰でも解ける (`Solution2`)
*   https://github.com/fhiyo/leetcode/pull/55/files
    *   辞書 + bisect (follow-up に対する解法): `Solution3`
    *   上記では `bisect_left` を使っているが、`bisect_right` だと `+ 1` しなくてよい。
*   https://discord.com/channels/1084280443945353267/1201211204547383386/1231637671831408821
    *   書き方のバリエーションとして。またこの正規表現による書き方面白い。正規表現は不慣れなので徐々に慣れたい。
        *   https://note.nkmk.me/python-re-match-search-findall-etc/
        *   https://note.nkmk.me/python-raw-string-escape/
    *   > これは、本当はエスケープしないといけないし、セキュリティ的に危ないという感覚は持っておいてください。(s に "." が含まれるなど。)
    *   s が複数来るなら、compile しておいたやつを使いたくなるだろうか: `Solution4`
        *   `self._pattern` とかに保存しておいて使い回す


```python
# 上記から引用
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ""
        for c in s:
            pattern += ".*" + c
        return re.match(pattern, t) != None
```

### step3

*   `step2.Solution1` が一番馴染みが良さそう。
