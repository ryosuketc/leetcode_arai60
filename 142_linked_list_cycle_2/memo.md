# 142. Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/description/

## Commends

### step1

*   最適解はうさぎとかめのやつなんだろうけど、hash set が想定解なのでそっちで書いてみる。
    *   https://github.com/ryosuketc/leetcode_arai60/pull/1/files#r2083815793
*   問題文からだとサイクルがないときに何を返せばいいのか最初よくわからなかった。とりあえず何も返さずに submit したら通ったからこれでよかったらしい。
*   `nodes_seen` とか `nodes_visited` とか naming ちょっと迷った。
*   最初 submit したとき、cur = cur.next 忘れてた

### step2
*   とりあえず hare and turtle やってみた
*   アルゴリズムうろ覚えで実装始めたけど割といくつか詰まった。ちゃんと脳内でアルゴリズム再生できてから実装しないと練習効果が薄い気がする
    *   `slow, fast = head, head` と初期化したのに、ループの冒頭で `if slow is fast` チェックして break してきた
    *   fast をリセットして再度回すときに、fast を 2 つずつ進めてしまった。
    *   ただ大まかな処理の流れは LeetCode の editorial の解答の感じだった。もっときれいな書き方あるのかな


```python
# pass
slow, fast = head, head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
        break
```

```python
# fail
slow, fast = head, head
while fast is not None and fast.next is not None:
    if slow is fast:
        break
    slow = slow.next
    fast = fast.next.next
```

*   他の人の PR 見てみる
    *   https://github.com/potrue/leetcode/pull/2/files

*   命名規則に関するコメント集を眺めてみる
*   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.fcs3httrll4l
これ割と新発見。まあ確かに production code でローカル変数として使っているの見たことない気がする？
> current は多くの場合、context のようなグローバルな設定などに用いられる傾向が強く、今注目しているもの、というつもりだと標準的用法からかなりずれを感じます。変数名は長ければ読みやすい訳ではないんです。previous, next との対比ならばまだしも。

