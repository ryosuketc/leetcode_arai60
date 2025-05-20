# 83. Remove Duplicates from Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## Comments

### step1

*   sort されてるんだし2つポインタつかって走査したいなあという感じではあったけど、実装楽で可読性高いかなと思ってセットを使うパターンでやってみた。結果、最後の node の処理とか (後半の for loop) むしろ冗長になった。
*   あるとは思ったけど後で調べたらこういうライブラリはあるらしい。とはいえ今回で使いたいかというと、今回は最後に append していくだけだしまあリストとセットを両方作ればいいかなと思う。remove とか pop しだすと、リストの方でその処理どうする問題がある (リストの途中の要素を削除したり、そもそもその要素を探したりすることになるので)。
    *   https://grantjenks.com/docs/sortedcontainers/sortedset.html
*   なんせ今回はポインタで解くほうが想定な気がする (sort されているし)
    *   とりあえず何も見ずに accept までやってみた。`step1_2.py`
    *   `next_node.next` ってなんか next が 2 個あってきもい


### step2

*   https://github.com/TORUS0818/leetcode/pull/5/files
    *   この辺見てると、そもそもポインタを 2 つ使うのは必須ではないのか
    *   直感的には処理済みの先頭、未処理の先頭を持つイメージだったので、step2でも2つポインタを持つように書いてみた。
        *   イメージ、先行する `node_next` は毎イテレーション動くが、`node` (処理済み) は、値が違うときにだけ進める (同じ時は `node_next` だけが進む)。
        *   最初、`node.next = node_next` は値が違うとき (if の中) でやっていたが、最後に重複するノードがある場合、最後のノードをアップデートできないので、`node.next` は毎回アップデートする必要がある。これを考えるとそもそもこのやり方シンプルでないしエラーになりやすいかもしれない。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            if current.next and current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
```

*   https://github.com/Fuminiton/LeetCode/pull/3/files
    *   こっちだと nested loop

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current_node = head
        while current_node:
            next_node = current_node
            """Replace the next node with a node
            that does not duplicate the current node"""
            while (next_node) and (current_node.val == next_node.val):
                next_node = next_node.next
            current_node.next = next_node

            current_node = current_node.next
        return head
```
