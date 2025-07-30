# 6. Zigzag Conversion

https://leetcode.com/problems/zigzag-conversion/

## Comments

### step1

*   3:00 くらい考えて問題の意味がわからなかったので解答の一部だけ見た。
    *   というのも、下がっているときは全部埋めるのはわかったのだが、上がっていくときにどこに文字列を置くべきかわからなかった
        *   -> 上がるときは斜めに上がっていく
*   これを理解した段階で解答のコードなとは見ず、再度考えた。
*   トータル 25:00 弱くらいで `Solution1` 書いた。
    *   最初、`numRows <= 1` のケースを考えていなくて WA
    *   また2次元リストに対する list comprehension を久しぶりに書いたので
        *   正: `c for row in zigzag_pattern for c in row`
        *   誤: `c for c in row for row in zigzag_pattern`
        *   としてしまった。いや、普通の for loop で書こうかとも思ったのだが。list comprehension でも普通のループと同じ順番なのね (右側が外側のループだと思っていた)
        *   正直 list comprehension そこまで好きではないのだが、今回は順番に出力するだけなので、別にリスト用意して (`result` とか) やるのはちょっと面倒だな、という程度の感覚。
*   コメントにも書いたがこの解き方だと、問題文にあるようなテーブルを作るのではなく、校舎のような compress された形を作ることになる。最終的には行ごとに出力するのでこれでも問題ない。
    *   問題文の形式でやりたければ、最初 `''` 埋めした2d list を作っておいて、`col_index` 的なものを保持していればできるはず。最後の文字列出力のコードは特に変える必要なし。

```
# Rather than this...
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Create this instead:
# P I N
# A L S  I G
# Y A H R
# P I
```

*   この実装だと、ループの最初、`s[0]` のときも `going_down` を flip することになるので、`going_donwn` は `False` で始める必要がある。最初は下に行くもの、という期待値なのでちょっと紛らわしい印象はある。
    *   `for i, c in enumerate(s)` として `i=0` だけ例外処理してもよいが、、
    *   `Solution2` 書いてみた。まあそんなに煩雑ではないか。ただコメントで補足くらいは必要そうだなという気がする。

### step2

*   https://github.com/Ryotaro25/leetcode_first60/pull/66#discussion_r2020118072
    *   > Java や Python など文字列が immutable な言語では重要な話ですが、C++ では、mutable で後ろに文字をつける分には大きな問題になりません。
    *   > 前後に付けたり分割したりなどする必要があるならば、Rope というデータ構造などを使えばいいですが、そこまでする必要があることは少ないです。
    *   へえ、そうなんだ。次から C++ をやる予定だから覚えておこう。
*   https://github.com/olsen-blue/Arai60/pull/61#discussion_r2040670667
    *   > 面白解法を考えはじめました。うーん、たとえば、itertools.batched とかどうでしょうか。
    *   > 長さcycleの部分文字列を切り出して、chunkでループする、ということなのですね。
    *   > https://docs.python.org/3/library/itertools.html#itertools.batched
    *   今回あまり深入りしていないが、`itertool` とか `functools` とかやっぱりちらほら知らない or 忘れているやつがある。
*   https://docs.python.org/3/reference/expressions.html#generator-expressions
    *   `''.join(c for row in zigzag_pattern for c in row)` とするのは、厳密には list comprehension ではなく generator だというのは脳内ではわかっていたが、さほど区別せずに使っていた。パフォーマンスとかの観点だとどちらがいいんだろう。
    *   List comprehensions: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
*   https://github.com/hayashi-ay/leetcode/pull/71/files
    *   3rd までの解放はわりと複雑だなと感じる。4th が私の解法に近いが、`going_down` の代わりに step という `+1` or `-1` の変数を管理している。stock の問題で似たようなのやったので、こういう increment / decrement をコントロールするような変数を使うのは step1 でも候補にあったがよい変数名がなかったので見送っていた。`step` はよさそう。
        *   `Solution1` 書いてみた。まあシンプルではあるが、読む負荷はちょっと高いかもしれない。
*   https://github.com/olsen-blue/Arai60/pull/61/files
    *    cycle 使った解き方、理念としてはわかっている (剰余を使って、挿入すべき index を探す) がやはりちょっと負荷が高い。
*   Generator を使うパターン
    *   https://github.com/saagchicken/coding_practice/pull/22#discussion_r2009413184
    *   https://github.com/saagchicken/coding_practice/pull/22#discussion_r2009508424
        *   > この問題、出題意図は、お手玉できるか、な気もします。
        *   > Generator は内部的には、ある種のコンテキストを持っていて、計算の続きに戻れるようにしています。だから、それなりに重いです。
        *   > そういうわけで、手続き型の手法で構造を組み合わせられるかが想定だろうなと思います。
    *   上記参考に `Solution2` 書いた。結構w借りやすい気もする。今回必要かというと微妙だが。
    *   `next` 使いたくないなあ、となんとなく思ったのでループで書いたら `WA` (`Solution3WA`)
        *   `num_generation` みたいなのを入れないと無限ループになる。
        *   それはともかく、よく考えるとそれはそうなるわという感じ。
    *   `Solution3AC` のように直した。うーん、まあこれなら `next` 使ったほうがいいな。

### step3

*   flip ではなく bool 値の代入で書いてみた (`Solution1`) が、個人的には flip のほうが読みやすく感じた (`Solution2`)。
