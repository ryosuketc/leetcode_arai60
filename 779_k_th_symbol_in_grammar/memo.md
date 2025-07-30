# 779. K-th Symbol in Grammar

https://leetcode.com/problems/k-th-symbol-in-grammar/

## Comments

### step1

*   recursion の問題だなーとは思いながら考えたけど明確な解法思いつかず。
*   とりあえず愚直な解法を実装してみたけど memory limit exceeded
*   n が 30 までということは、2^30 文字の文字列を保存することになる。
    *   `sys.getsizeof("a") -> 50` (bytes) とかなので、途方もないサイズになる
    *   https://docs.python.org/3/library/sys.html#sys.getsizeof
*   LeetCode によると binary search tree と recursion の解法があるみたい。ただ説明が長いので細かく見ずに一旦他の人の解答を探る。
*   https://github.com/fuga-98/arai60/pull/46/files

*   ビットを使った解法
    *   あービットによる解法あったのか。以前解いたときは、ビットで解けそうだなくらいの感覚だったんだけど、今回は出てこなかった。
    *   https://github.com/olsen-blue/Arai60/pull/47#discussion_r2002307405
        *   > あ、この問題もっとマクロな話をするとビットカウントの偶奇になっていますよ。二分木を考えて、右に行くとビットが反転して、左に行くとしないということですね。
        *   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.adit16u7jkla
    *   `int.bitcount()`
        *   https://docs.python.org/3/library/stdtypes.html#int.bit_count
        *   知らんかった。bin(int).count() でも代用はできる
        *   > kの値にどう結びつくのかイメージできずでしたが、k-1 の二進数表記はルートからの移動パターンなんですね。k=5 (k-1=4, 二進数 100)だと、右(1)->左(0)->左(0)ですね。なので、k-1のビットを数えて偶奇を調べれば良いんですね。

```
0
01
0110
01101001
...
```

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k - 1).bit_count() & 1
```

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        # k % 2 == 0 (偶数) のときビット反転、奇数のとき反転しない
        return self.kthGrammar(n - 1, (k + 1) // 2) ^ (k % 2 == 0)
```

```
self.kthGrammar(2, 1) -> call self.kthGrammar(1, 1)
self.kthGrammar(1, 1) -> return 0
```

```
self.kthGrammar(2, 2) -> call self.kthGrammar(1, 1)
self.kthGrammar(1, 1) -> return 0
```

*   https://github.com/olsen-blue/Arai60/pull/47/files
    *   > kの偶奇が大事そう?? 子ノード(n, k)を考えると、kが奇数の時、その親ノードと同じ値になる。kが偶数の時、その親ノードから反転した値になる。

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        if k % 2:
            return int(self.kthGrammar(n - 1, (k + 1) // 2))
        else:
            return int(not self.kthGrammar(n - 1, (k + 1) // 2))
```

### step2

*   https://leetcode.com/problems/k-th-symbol-in-grammar/editorial/
    *   ここまで読んでイマイチ腹落ちしないので、割と丁寧そうな LeetCode の解法を改めて見てみる。
    *   Binary Search を素直に実装した `Solution1` ふつうにわかりやすい。LeetCode のをきれいに書き直した。
    *   前半分、後ろ半分でビットが入れ替わっていることを利用した `Solution2`。これもわかりやすい。
        *   0 <-> 1 の反転には色々方法が。`1 - x` とか `1 ^ x` とか。
    *   k - 1 のビット数カウント
        *   k から、row のノード数の半分を引いていき、最終的に 1 になるまで繰り返す
            *   `k - 2^a - 2^b - ... = 1`
            *   `k - 1 = 2^a + 2^b...`
        *   > The number of bits in number k is logk.
        *   一応この説明でなんとなくはわかるのだが、
            *   なぜ `k - 1` なのか
                *   zero index になおしているのはそうだけど、なぜ k の偶奇で答えがわかるのか。n は？
                *   結局ビットが 1 である回数 == 反転 (flip) した回数？

### step3

*   ビットの解法が腹落ちしきらないので一旦納得できた `Solution2` のパターンで練習
