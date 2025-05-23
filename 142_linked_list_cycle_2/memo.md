# 142. Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

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

### step3
*   他の人の PR 見て reifine
    *   https://github.com/potrue/leetcode/pull/2/files
    *   https://github.com/rieuky/arai60/pull/2/files
*   命名規則に関するコメント集を眺めてみる
    *   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.fcs3httrll4l
    *   これ割と新発見。まあ確かに production code でローカル変数として使っているの見たことない気がする？

> current は多くの場合、context のようなグローバルな設定などに用いられる傾向が強く、今注目しているもの、というつもりだと標準的用法からかなりずれを感じます。変数名は長ければ読みやすい訳ではないんです。previous, next との対比ならばまだしも。

*   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.jfs03xpyyrfl の逆回しにする説明がどうしてもピンと来ない…

個人的には

```
A: スタートから合流地点までの長さ
B: サイクルの長さ (合流地点を起点とする円の円周)
x: 衝突地点から再度合流地点に行くまでの長さ
```

として

```
Slow が進んだ長さ = A + (B - x)
Fast が進んだ長さ: A + 2B
Fast = 2 * Slow の速さで進むので
A + 2B = 2 * (A + (B - x))
x = A
```

なので、スタートから合流地点までの長さ = 衝突地点から再度合流地点に行くまでの長さで、したがってスタートと衝突地点からそれぞれ始めて同じ速さで進むと合流地点でぶつかる、という説明だとまあ方程式がそうなるんだからというので理解できる。正直あまり直感的には理解できてない…

*   step2, step3 にある書き方でいくつか類似パターンを試したけど、while ... else ... がなんとなくしっくりくる。else を使わないパターンだとループを抜けたあとに `if fast is None or fast.next is None:` と、ループの条件と似たようなものをチェックしないといけないのが繰り返している感じになって違和感。
*   ただ、else 使うパターンだと、Y ならばこう処理する (do_if_y) の処理の流れが、else 部分によって分断される見た目になるのでちょっと不自然な気はする。この問題だと、2 つめの while は関数に切り出して break は使わずに処理したほうがいいのかなという気もする。

```python
while X:
    if Y:
        break
else:
    return do_if_no_break_in_loop()

do_if_y()
  
```

*   関数に切り出すならこんなんとか。関数名はもう少しちゃんとしたいけど。
    *   以下の例だと `_detectCycleAuxiliary` の `fast` argument を rebind (`fast = fast.next`) してるけどこれっていいんだっけ。オブジェクト自体を mutate しているわけではないから副作用はないけど、arg を rebind するの、なんか良くない気がするけど調べても良くないかぱっと出てこなかった。muration の話なのかな。

```python
class Solution:
    def _detectCycleAuxiliary(self, head, fast):
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return self._detectCycleAuxiliary(head, fast)
        
        # implicitly return None - successfully looping through means there is no cycle.
```