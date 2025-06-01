# 111. Minimum Depth of Binary Tree

https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

## Comments

### step1

*   6:30
*   max depth の問題に引っ張られて謎のコードを書いていた…(もちろん wrong answer `SolutionWA`)
*   正しくは leaf のときに min depth をアップデートするので `Solution` のようになる。
*   min_depth の初期値、float('inf') でよいのかは疑問。production ではあまり見ないようにも思うけど。
*   最後の return の処理もちょと迷う。要は root が None だったときの処理で
    *   三項演算子を分かりづらい (以下の例のほうが直感的)
    *   root is None のときそもそも何を返すべきか
        *   冒頭で early return しておく方法もある。その方が意図は明確そう
        *   論理的に、値としては 0 が妥当かなとは思うが。

```python
if min_depth == float('inf'):
  min_depth = 0
return min_depth
```

### step2

*   > そうですね。木の高さを求めるときには、上から数字を配っていくか、下から集めてくるかの2方向があって、それぞれ再帰で書くか、スタックとループで書くか、がありますね。
*   > はい。再帰とスタックの書き換えくらいだと私も思います。しかし、この二つの変換が息を吐くようにできるとだいぶ分かっている感じがするので大事だと思います。
    *   https://discord.com/channels/1084280443945353267/1196472827457589338/1237988315781664770
*   相変わらず下から集めてくる方はいまいちピンときてない。一回休み (https://github.com/ryosuketc/leetcode_arai60/pull/21)。
*   `math.inf == float('inf')` らしい。
    *   > A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').
        *   https://docs.python.org/3/library/math.html#math.inf
    *   positive / negative inf を一気にチェックできる `isinf` というのがあるようだ
        *   https://docs.python.org/3/library/math.html#math.inf

```python
In [96]: math.inf == float('inf')
Out[96]: True
```

*   step3 の最初に思いついて `if all(children, lambda x: x is None):` とか書いてみる
    *   あれ、all は関数取らないんだったか
    *   関数取るのは `filter` だけど引数の順番が逆…function -> iterable
        *   https://docs.python.org/3/library/functions.html#filter
        *   `filter(function, iterable)`
    *   一応 `if  len(list(filter(lambda x: x is None, children))) == 2:` あたりが動くけどまあやり過ぎ
    *   とか考えてたけど Python で書くならふつう `if not any(children)` か。これなら割といいかも。まあ、`not child` で None 判定するのか、`is None` なのかの違いはあるかもだけど…

### step3

*   3:30 (typo とか、list に append するときに tuple にし忘れていたりしてエラー) -> 3:00 (変化なしなので打ち切り)
