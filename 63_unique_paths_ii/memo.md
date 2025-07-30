# 63. Unique Paths II

https://leetcode.com/problems/unique-paths-ii/

## Comments

### step1

*   基本 unique path を改造して解けそうだと考える
    *   上と左の paths を足す。
    *   obstacle だったら 0
*   右か下にしか動けないので、セルを左上から右下に向けて探索したとき、obstacle があったらそれより右に行く手段はなくなる (0)。
*   ある程度動きそうなアルゴリズムであるのを脳内で確認して実装。
*   submit して WA (`SolutionWA`)
*   よく考えると、> 右か下にしか動けないので、セルを左上から右下に向けて探索したとき、obstacle があったらそれより右に行く手段はなくなる (0)。 の部分を正しく実装してないことに気づく。
*   何度か試行錯誤して、16:00 くらいで、`SolutionAC` に修正して AC
*   結局ゼロ初期化しているので、obstacle があったらそこで走査を打ち切ればよい (最初の行、最初の列の処理)
*   最初の行、最初の列以外のループでは、obstacle でなければ左と上を足す。obstacle なら 0
    *   ここを書いていて、この処理不要だと気づいた (`SolutionAC2`)。

```
                else:
                    paths[row][col] = 0
```

*   一応 constacnt space のパターンで書き直すかと思ったけど WA (`SolutionWA2`)
    *   大分時間経っていたので他の解答を見ることにする

### step2

*   https://github.com/Fuminiton/LeetCode/pull/34/files
    *   自分は最初の行と最初の列は別に処理するものとしていたけど、なるほど、ループ内で分岐する書き方もあるか。
    *   width / height にすると、ループのときのインデックス変数の名前に悩むので、rows / cols にしていたが、height / width だと x / y あたりが使えるのか
*   https://github.com/olsen-blue/Arai60/pull/34/files
    *   問題の制約から大丈夫だろうと割り切っていたが、gobstacleGrid のサイズについては冒頭にチェックしてもいいのかも。
    *   > 1次元DPもあった。obstacleがあるかどうかを２次元で見ているので、テーブルだけ1次元にするの、なんか嫌。
        *   1d DP の解法 (`step1.SolutionWA2`)、正しく書けていないが、これは私も思った。obstacleGrid との不整合がややこしい。
        *   `step2.SolutionWA` を書いてみたけどやはり動かない。`obstacleGrid =[[0],[1]]` みたいなインプットで落ちる (内側の `for col in range(1, cols):` が実行されない)
            *   エッジ初期化のパターンで 1d DP って難しいのかな？
            *   かといって cols == 1 のときの処理で分岐させたくはないし
*   https://github.com/hayashi-ay/leetcode/pull/44/files
    *   この辺みると 1d DP はエッジ処理ではなく for ループで処理するやり方
    *   OBSTACLE 変数置くの割と共通認識っぽい。個人的には 0/1 だしグローバル汚したくないし、わざわざかなと思ったけど一応グローバル変数でいくかな
        *   どうでもいいが、LeetCode だと `Solution` class なので、クラス変数として定義するのは違和感。かといて関数内で定義するのも呼び出しのたびに初期化されて無駄だし、消去法的にグローバル変数。
*   色々見たが結局エッジ初期化する 2d DP が一番しっくりきた。

### step3

*   3:30 - 4:00 程度
