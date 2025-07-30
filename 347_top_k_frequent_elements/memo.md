# 347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/description/

## Comments

### step1

*   最初 stream の問題なのかと勘違いしていた
    *   その場合、(freqency, item) の tuple を要素に持つ min_heap とか作ろうかなと思ったけど、frequency が更新されるたびに heap 内の要素を検索して削除して追加しないといけないから非効率なように思う
    *   …あたりまで考えて stream ではないことに気付いた (とはいえ、これが stream だったらどう解くんだろう)
*   とりあえず 7:30 くらいで書いた (`Solution`)。可読性のかけらもないただのスクリプトなのでこれは良くない。
    *   Python っぽくはあるんだけど lammbda とか list comprehension とか濫用は良くない気が。
*   `Solution2` で可読なように書き直した。

### step2

*   このあたり眺めた
    *   https://github.com/Fuminiton/LeetCode/pull/9/files
    *   https://github.com/TORUS0818/leetcode/pull/11/files
*   `step1.Solution2` では lambda を使うのは避けて、frequency (count) を第一置要素の tuple に変換した (tuple 同士の比較は、第一要素から行うので)。
    *   lambda x: x[1] は itemgetter(1) のようだ
        *   https://docs.python.org/3/library/operator.html#operator.itemgetter
*   step1 の段階で heap を使う実装も考えたんだけど、少なくとも計算量の観点では sort を変わらない (まあ heap sort もあるわけだし) ので、慣れている sort を選んだ。dict <-> list の変換が煩雑になるからという理由で heap を選んでいる方もいたが、実際この 2 つは好みな気がする (?)。
*   `num_counter` とか `count_and_nums` という命名がよいのではとコメントされていた。たしかに `frequency` と `count`、意味が重複している…

### step3

*   2:20 -> 1:30 -> 1:30
*   defaultdict に関する議論を見かけた。結構面白い
    *    https://discord.com/channels/1084280443945353267/1225849404037009609/1228028878589657150
