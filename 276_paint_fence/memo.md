# 276. Paint Fence

https://leetcode.com/problems/paint-fence/

## Question

You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.

Example 1:

Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
Example 2:

Input: n = 1, k = 1
Output: 1
Example 3:

Input: n = 7, k = 2
Output: 42

Constraints:

1 <= n <= 50
1 <= k <= 105
The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.

## Comments

### step1

*   しばらく考えて、最初の 2 つが `k`, `k * k` 通りあることはわかったが、それ以降の関係性を出せなかったので解答を見た。
*   今のフェンス (`i`) を直前のフェンス (`i - 1`) と違う色で塗る -> `(k - 1) * totalWays(i - 1)`
    *   これはすぐわかる
*   今のフェンス (`i`) を直前のフェンスと同じ色で塗る
    *   `i - 1` (直前のフェンス) が、`i - 2` と違う色だった場合だけ可能。
    *   つまり上の式に当てはめるとき、今のフェンス (`i -1`) を直前のフェンス (`i -2`) と違う色で塗る、と読み替えられるので、`(k - 1) * totalWays(i - 2)`
*   最初、`return total_ways[-1]` としてしまった。これだと n = 0 とか 1 のときに対応できない

### step2

*   LeetCode の解答を参考に色々書いてみる
*   再帰で top down に書く (`SolutionManualMemo`, `SolutionLruCache`)
    *   関係式と base case さえわかればさらっと書ける
*   個人的に DP は (少なくともこの問題は) bottom up の方が直感に合っていて好き (`SolutionBottomUp` - step1 と同じ)
    *   bottom up といえば space O(1) にする方法があったの発想から漏れていた (`SolutionBottomUpConstantSpace`)
*   LRU Cache 関連
    *   https://docs.python.org/3/library/functools.html#functools.lru_cache
    *   `maxsize`
        *   > If maxsize is set to None, the LRU feature is disabled and the cache can grow without bound.
        *   今回だと n <= 50 だから maxsize も 50 あれば事足りる。
        *   ただ実際に試すと `lru_cache(2)` 以上なら accept された (1 にすると TLE)。LeetCode そんなに大きいテストケース入れてないのかな？
    *  `typed=False` という引数もあるの知らなかった。LeetCode 文脈だとそんなに使わなさそうだけど、どういう use case なんだろう
*   https://github.com/hayashi-ay/leetcode/pull/17/files
    *   LRU Cache を自作していた。メモ化自体は `lru_cache` デコレータを使わなくても `SolutionManualMemo` のやり方でできると思っていたけど、デコレータの方を書くというのは考えていなかった。
    *   LRU Cache の実装自体は、NeetCode にもある: https://neetcode.io/problems/lru-cache?list=neetcode150 ので今回は省略。
        *   LRU 実装はこのあたり: https://discord.com/channels/1084280443945353267/1201211204547383386/1220666008881336331
        *   `OrderedDict` の実装は Doubly Linked List: https://github.com/Fuminiton/LeetCode/pull/30#discussion_r2040649727
    *   `SolutionMyDecorator`: この書き方だと AC
    *    デコレータはただの syntax sugar なので、と思って、`return memo(total_ways)(n)` と書いてみると n=43 で TLE した。何かの overhead があるんだろうか？ (`SolutionMyDecoratorTLE`)
        *   Gemini 賢い。`SolutionMyDecoratorTLE` の書き方だと、再帰呼び出しに使う関数はメモされていないんだ。
        *   `SolutionMyDecoratorNoSyntaxSugar` のように  `total_ways = memo(total_ways)` とするとよい。
    *   デコレータ自体に引数を渡す場合はさらにネストを 1 階層深くする。上記 PR 参照
        *   https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e
    *   簡単なデコレータは書けるが、デコレータ自体に引数を与えたりはまだそんなに自信がない
*   もう少し他の人の解答も見たかったが、結構時間かかったので一旦このあたりで。

https://github.com/hayashi-ay/leetcode/pull/17/files から引用させていただいた。参考用。

```python
class Node:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.sentinel = Node(1, 1)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self.remove(node.key)
        self.insert_front(node.key, node.value)
        return node.value

    def remove(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[key]
        self.size -= 1

    def insert_front(self, key, value):
        node = Node(key, value)
        next_node = self.sentinel.next
        self.sentinel.next = node
        node.prev = self.sentinel
        node.next = next_node
        next_node.prev = node
        self.size += 1
        self.cache[key] = node
        if self.size > self.capacity:
            last = self.sentinel.prev
            self.remove(last.key)


def my_lru_cache(maxsize=1):
    def decorating_function(func):
        nonlocal maxsize
        if maxsize <= 0:
            maxsize = 1
        return _my_lru_cache_wrapper(func, maxsize)
    return decorating_function


def _my_lru_cache_wrapper(func, maxsize):
    cache = LRU_Cache(maxsize)
    def wrap(*args, **kwargs):
        result = cache.get(args)
        if result is not None:
            return result
        result = func(*args, **kwargs)
        cache.insert_front(args, result)
        return result
    return wrap
```


### step3

*   全体としてはやはり bottom up が好き。constant space に書き直すのは必要があればやるが、配列を確保するやつの方が何をしているかわかりやすいと感じた。
*   step1 のように `append` していくのが Python っぽい気もするのだが、DPだと何番目の要素をアップデートしているかがわかりやすくなるので `total[i] = ...` としたほうが読みやすそう。
*   今回は 0-index で解いた。1-index より読みやすい気がする (ちなみに n >= 1 が保証されており、n == 0 は handle しなくてよい)。
