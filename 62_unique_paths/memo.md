# 62. Unique Paths

https://leetcode.com/problems/unique-paths/

## Comments

### step1

*   DP の問題なのでまあ DP でという先入観はありつつ、再帰でも解けそうだなという感じはする。
    *   ただ再帰で具体的にどうやるまでの落とし込みまでは行かなかった。それまでに発見した path の数をどうやって引き継ぐか…
    *   DP については、上か左のマスの合計値になるというのはすぐわかった
*   5:30 で `Solution1` 書いた。
    *   m, n で行列の大きさ書くの嫌いなので、変数に入れた
*   このやり方だと space O(cols) には簡単にできそうだということで、他の解答見る前にとりあえず `Solution2` を書いた。
    *   変数名はちょっとイケてないかもしれない。
    *   一番最初 `paths = [1] * cols` と、すべて 1 で初期化するのはちょっとわかりにくいかも。実際には一番最初の要素だけ 1 であればよく、それ以降はアップデートされるので実際使わない。

### step2

*   https://github.com/nittoco/leetcode/pull/26/files
    *   メモ化再帰でも実装できる。step1 ではしっかり検討できていなかったが、実装は思ったより簡単だった。
    *   https://github.com/olsen-blue/Arai60/pull/33#discussion_r1966730122
        *   再帰の計算量
        *   > 最終的にすべて return 1 になっていて、それが木のように足されていますね。だから、計算量は (n+m)Cm になるはずです。
        *   この部分が割と理解しにくかった。木構造からどうやって `(n+m-2)C(m-1)` が出てくるんだろう。
            *   木構造をベースに考えると、完全二分木なら葉の数は `2^(tree height - 1)` になる。今回 tree height は最大で `m + n - 2` くらいかな？ 
                *   m, n 両方が 1 に近くなるまで引く。たとえば (3, 4) だったとき、m だけから引いて (1, 4) を作ると、高さは `m - 1` で、m, n からバランスよく引いて (1, 2) とか (2, 1) を作ると `m + n -2`、とか。
                *   なので葉の数は `2^(min(m - 1, n -1)) <= leaves <= 2^(m + n -2)` くらいになる。
            *   一方で、葉の数 = 問題の経路の数であると考えると、数学的に `(m+n-2)C(m-1)` であるのはわかる。結局動く回数 `m + n - 2` (a) のうち、どこで縦に動くかを決める (残りは横) (b) ので、aCb の問題になる。
            *   上記それぞれはまあｗかるのだが、木構造から combination の式に直接辿り着く方法がよくわからない。
        *   https://github.com/hroc135/leetcode/pull/33#discussion_r1899013887
            *   フィボナッチ数列の計算量。このあたりはまだそんなに見ていない (TODO: robber のときに改めて確認する) が、今回もフィボナッチ風の問題設定だというのは理解できる。
*   https://github.com/saagchicken/coding_practice/pull/19#discussion_r2007873330
    *   メモリ配置と速度の話
*   https://github.com/fuga-98/arai60/pull/33#discussion_r2040681343
    *   これはちょっと笑った。なるほどたしかにコピーしていると 1D DP の解法として動くのか
*   https://github.com/Fuminiton/LeetCode/pull/33#discussion_r2052721643
    *   この認識はあって使っているので大丈夫そう
*   LeetCode 解答
    *   math で、combination の問題として解く方法もある。こちらは考えていなかった。
    *   階乗の計算量に関する話よくわからん
    *   https://qiita.com/AkariLuminous/items/1b2e964ebabde9419224
        *   これの「2. odd_partを数式で表す」あたりですでに詰まったのでまた後ほど見てみる (TODO)。
*   https://github.com/olsen-blue/Arai60/pull/33/files
    *   上記でも参照しているが、改めて読んでいると、space O(1) にする場合、私の step1 だと 2 行分保持していたが、1 行でも足りる。
    *   rows, cols よりも height, width の方が多い気がしたのでそっちで書いてみた (`SolutionDP`)。
        *   `for position in range(1, width)` のときのインデックス変数にどういう名前をつけるか迷う

### step3

*   1d DP がすっきり書けていいような気がした。
