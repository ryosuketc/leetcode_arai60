# 104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

## Comments

### step1

*   最初 `SolutionAC` の方で書いていたんだけど、これだと、(None, 1) のような要素が append されるので、なんか None に対して depth がついているの嫌な気がした。ので、`SolutionRuntimeError` に書き直した。
*   よく考えると、root が None のケースを考慮していなくて Runtime Error。その後すぐに `SolutionAC` に書き直した。4:50 くらい。
*   大雑把に DFS、BFS を考えていて、再帰で書こうかと思ったのだが、再帰で書くときに depth の引数渡すのがなんとなく面倒だったのと、10^4 の制約でデフォルトの recursion limit 超える気がしたので iterative DFS にした。
    *   > The number of nodes in the tree is in the range [0, 104].

### step2

*   https://github.com/nittoco/leetcode/pull/14/files
*   https://discord.com/channels/1084280443945353267/1227073733844406343/1236235351140339742
    *   私の方法は上から配る方だと思うが、概念として下から戻す方法が存在するのはわかるものの、今回どうやってやるのかよくわからない。このへん読んでみたが、結局なにをどうしているのかよくわからん…。一旦次に進む。
        *   https://discord.com/channels/1084280443945353267/1227073733844406343/1236695050902048899
    *   というかそもそも下から戻す再帰だいぶ苦手かも。
*   > 訪れているかの判定を次の再帰に任せた場合、やや処理速度が落ちる点は気にしたほうが良いと思います。理由は、関数の呼び出しが、一般的に、コストがかかる処理だからです。個人的には再帰関数呼び出しの前に判定したほうが良いと思います。
    *   https://github.com/sakupan102/arai60-practice/pull/22#discussion_r1590605423
    *   これだと、`SolutionRuntimeError` の冒頭に `if root is None` を足せば動く
*   感覚として、個人的には再帰で書くより stack で iterative に書くほうが好きらしい。

### step3

*   step2 で、これといっては直したいところもなかったので、一旦何回か書いてみて馴染まないところがあるか考えることにした。
*   1:10 -> 1:10 (特に変化がないので打ち切り)
