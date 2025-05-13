# 83. Remove Duplicates from Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## Comments

### step1

*   sort されてるんだし2つポインタつかって走査したいなあという感じではあったけど、実装楽で可読性高いかなと思ってセットを使うパターンでやってみた。結果、最後の node の処理とか (後半の for loop) むしろ冗長になった。
*   あるとは思ったけど後で調べたらこういうライブラリはあるらしい。とはいえ今回で使いたいかというと、今回は最後に append していくだけだしまあリストとセットを両方作ればいいかなと思う。remove とか pop しだすと、リストの方でその処理どうする問題がある (リストの途中の要素を削除したり、そもそもその要素を探したりすることになるので)。
    *   https://grantjenks.com/docs/sortedcontainers/sortedset.html
*   なんせ今回はポインタで解くほうが想定な気がする (sort されているし)
    *   とりあえず何も見ずに accept までやってみた。`step1_1.py`
    *   `next_node.next` ってなんか next が 2 個あってきもい