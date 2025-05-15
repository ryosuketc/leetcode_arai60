# 82. Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

## Comments

### step1

*   head 自体削除される可能性があるので dummy なり sentinel なり置かないと解けない
*   dummy の value を何にするかちょっと迷った (実際に存在しうる範囲内の値にすると重複排除に影響するのでは、と考えた)。最終的になんでもよさそうだから適当な値 (範囲内) にした。
*   謎に 20 分くらいはまった (動かない) ので、ひとまず答え探し
    *   脳内でステップ走らせてみようとしたがなんかハマった


### step2
*   答え見て気づいたけど、そもそも step1 の実装だと、注目している要素は2つ - node と、その次の node。でもよく考えると、最新の dup がない node を持っておかないと、dup をスキップできない。
    *   頭でやるときは自明 (重複ないのが確認できている最後の node をとっておいて、重複がきたら全部スキップしてその次の重複がない node とつなげる) なんだけど、プログラムで書こうとするとなぜかハマってしまった。頭で (人間が) やることをそのままプログラムでできるか、という意識が大切かも (コメント集に似たようなことを見かけた)
*   dummy という名前はふわっとしすぎな気がする。linked list だと sentinel か もしくは dummy_haed が良さそうな気がする
    *   sentinel、日本語だと「先頭や最後尾」とあるが、英語だと 「terminator」なので、先頭に置くやつは sentinel と呼ばないのだろうか

https://ja.wikipedia.org/wiki/%E9%80%A3%E7%B5%90%E3%83%AA%E3%82%B9%E3%83%88

> 線形リストには「ダミーノード」または「番兵ノード; sentinel node」と呼ばれるものが、リストの先頭や最後尾に置かれることがある。番兵ノードにはデータは格納されない。

https://en.wikipedia.org/wiki/Sentinel_node

> Sentinels are used as an alternative over using NULL as the path terminator...

*   dummy は値を持たない方がやっぱりいいので None にしようかな。ListNode.val が int | None を期待しているのかわからないけど。。
*   上記コンセプトレベルで理解した状態で一回書いてみたが結局詰まったので再度答え確認しつつ refine してみた。

### step3

*   このあたりを参照した
    *   https://github.com/Mike0121/LeetCode/pull/40/files
    *   https://github.com/nittoco/leetcode/pull/9/files