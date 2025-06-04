# 102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## Comments

### step1

*   level order traversal、BFS そのものなので BFS する
*   node 数の制約は 2000 なのでメモリに積んでいって特に問題はないはず
*   書き始める。最初 queue (deque) で書きはじめたけど、書いている途中でふつうの for loop でよいのではという気がしてくる (`for node in current_level` のところ)
*   8:30 くらいで書き上げ、2 分くらい脳内で Example のテストケース走らせてみて良さそうだったので submit。10:30 で accepted
*   これ、最初はもっと単純だと思っていたんだけど、書いているうちに`result`, `current_level`, `next_level`, `nodes_in_this_level` と、4 つリストを管理しないといけないことに気づいた。もっとシンプルに書けるのだろうか。

### step2

*   step1 解答の時点でフォーマットとか変数名とか、大きく直したいところはなさそうなので、他の解答を見てみる。
*   queue を最初にやったときにあれ書けないなと思って for に変更したのは、queue に node しか積んでいないからだった。実際は level (index) を積んでおいて、対応するレベルの index に node.val を append していく。
    *   https://github.com/hayashi-ay/leetcode/pull/32/files
    *   こちらの方がループが浅くていい感じな気はする。が、正直どちらでもいいなあ、という気はする。読む負荷はこちらのほうが低いかな？
*   step2 に自分で書いてみた。なぜか途中の `if len(result) <= level:` の条件判定で、不等号の向きとか、等号を入れるか、level + 1 するかとか、level を 0-index にするか 1-index にするかとか色々考えてハマって 5:00 くらい？悩んだ。最終納得して submit した。
    *   > 1段だけしか拡張しなくても例外が投げられることがないことに気がつくパズルを解かせる必要ないですよね。
        *   https://discord.com/channels/1084280443945353267/1200089668901937312/1211248049884499988
        *   なるほど、個人的には 1 段ずつしか拡張されないことは設計上自明なのでよいかなと思っていたが、確かに初見で読む側からすると while で保証されている方が認知不可が低い。
    *   最初 for ループで書こうと思っていたけど、node, level を入れる while の方がネストが浅く、変数が少ないので読みやすい。

```

### step3

*   3:30 -> 3:15。2 回書いてみたがそんなに変更はなさそう。
