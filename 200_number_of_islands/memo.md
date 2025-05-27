# 200. Number of Islands

https://leetcode.com/problems/number-of-islands/description/

## Comments

### step1

*   解答見ずに 10:30 で accepted
*   最初、0, 1 が文字列であることを見逃していた (int だと思っていた)
*   visited を関数の arg として渡すか、outer 関数 (numIslands) で定義してそのままアクセスするか迷った。関数内関数を定義するときにはどちらがよいのだろう (grid は関数内からアクセスしているのだし、visited も統一して良かった気もする)。
*   row, col が範囲内か、visited か、0 か、など再帰の終了条件は `traverse_island(row - 1, col, visited)` など個々のを呼ぶ前に逐一チェックする方法もあるが、まとめた方がきれいだと思う。
*   DFS でやる方法くらいしか思いつかなかった。BFS でもできそうではあるけど、1 つの island を全部探索し終わって次に行くのが自然な気がする
*   再帰の計算量正直よくわかってない…

### step2

*   https://google.github.io/styleguide/pyguide.html#26-nestedlocalinner-classes-and-functions
    *   この間も見たのだが、今改めて見るとちゃんと理解できてない箇所があったようだ
    *   > Avoid nested functions or classes except when closing over a local value other than self or cls
    *   これ逆に言うと、self, cl 以外の local value を close over するときは使っても良いという話
    *   前回、close over ってなんのことかよくわかってなかったのだが、closure のことか
        *   https://www.learnpython.org/en/Closures
    *   ならまあむしろ visited も引数で渡すより closure を使って外部関数の方にアクセスしたほうがいいか。

良さげな公式 doc がないので Gemini に聞いてみた

> 内部関数とは、ある関数やメソッドの内部で定義される関数のことです。内部関数は、それが定義された外側の関数（エンクロージングスコープ）のローカル変数に読み取り専用でアクセスできます。この仕組みをクロージャ (closure) と呼びます。

```python
def outer_function(x):
    # x は outer_function のローカル変数
    def inner_function(y):
        # inner_function は外側のスコープの変数 x を参照できる（クロージャ）
        return x + y
    return inner_function

closure_instance = outer_function(10)  # x に 10 が束縛される
result = closure_instance(5)           # y に 5 が束縛され、10 + 5 が実行される
print(result)  # 出力: 15
```

*   関数内関数から外側の関数の変数 (visited) を mutate するのはいいんだったか…
*   スレッド並列性？
    *   https://github.com/colorbox/leetcode/pull/31/files#r1881098955
*   どのタイミングで範囲外をチェックするかの議論あった。同じことを考えていた (traverse_island) の中、しかも冒頭でやったほうがよい、という話。
    *   https://github.com/sakupan102/arai60-practice/pull/18#discussion_r1582241335
*   再帰の深さの話合
    *   > 今回の制約上、m,n は最大で 300 なので、再帰の深さは最大 90,000 になる可能性がある。
    *   > 上、下、右、左の順序で再帰していくので、確かにこれは場面全部を蛇腹状に埋める形で再帰が深くなっていきますね。
    *   https://github.com/tarinaihitori/leetcode/pull/17#discussion_r1839410598
    *   これ踏まえると Python の recursion_limit (== 1000) を超える可能性がある、という話。もしくは再帰でなく stack で実装するか。
    *   https://github.com/Fuminiton/LeetCode/pull/17#discussion_r1984361170
*   Union Find もあるんだった。定期的に勉強しては忘れている…TODO: あとで復習
    *   https://github.com/ichika0615/arai60/pull/9/files
    *   https://github.com/Hurukawa2121/leetcode/pull/17/files
    *   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.p4yi13m12dqu
    *   なんかときどき見ている動画 (path compression もカバーしていたはず): https://www.youtube.com/watch?v=wU6udHRIkcc
*   DFS で行こうとは思ってちょっと整えてみた (`SolutionDfs`)。
*   recursionlimit をいじるのが気に食わないので iterative DFS にした (`SolutionIterativeDfs`)

### step3

*   結局今回、DFS、BFS、Union Find のどれがいいのかはよくわからん。個人的に grid traversal 系は DFS が慣れてるんだけど
*   5:30 -> 4:30 -> 3:40
