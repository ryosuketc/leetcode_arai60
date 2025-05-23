# 206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/description/

## Comments

### step1

*   適当に stack で書いてみたけど、なぜか Memory Limit Exceeded する。20 分くらい悩んだけどよくわからんので一旦放置。
    *   `reversed_node.next = previous` の行が原因っぽいけど
    *   もともと(Arai 60 だと stack の問題だとマークされている先入観もあったと思うが) stack で解いた方がきれいかなと想像していたが、意外に長くなって読みづらいかなという気もした。
    *   追記: 最後に (l29) `previous.next = None` してなかった。最後の node の処理が必要。これをしないと、こちらのプログラムは terminate するが、LeetCode 側で評価するときに無限ループになってしまう。
        *   テストケースを "最後まで" ちゃんと走らせていれば早く気づいたかも。簡単なやつだと思ってざっと走らせて、コードは論理的に正しいはずなんだけどなーというので詰まっていた。
*   pointer で書いた。`Solution2`
    *   1:00 くらい
    *   Python だと `tmp` なしでかけるけど、評価の順番は大事。
    *   以下 3 が動かなくて 5 分くらい悩んでしまった。どうやらこのコメントの一部を 100% 理解できていなかったらしい。
        *   https://github.com/ryosuketc/leetcode_arai60/pull/1#discussion_r2083884311
        *   よくよく考えると、右辺はまず最初にすべて評価され値が決まるけど、assignment は左から順に行われるので、以下のように、意図しない node オブジェクトが変更されてしまう。
        *   1. 右辺の値は先に決定 (計算) される 2. 左から順にアサインされる のうち、1 は理解していたけど、2 について意識しきっていなかったのかも。

```python
# 1. これは動く
node.next, prev, node = prev, node, node.next

# 2. これも動く (上のコードと等価)
tmp = node.next
node.next = prev
prev = node
node = tmp

# 3. これは動かない
prev, node, node.next = node, node.next, prev
```

たとえば None -> 1 -> 2 -> 3
の list を処理するとき、
prev = None, node = 1 で処理すると、右辺は順に

1, 2, None

と評価される。これが、左から順に

```python
prev =  1
node = 2
```

と処理され、最後に

```python
node.next = None
```

になる。このとき node = 2 だから、2 の next が None になってしまう。

### step2

*   step1 から、明らかに pointer を使うほうが速く書けるしきれいなように思うので、pointer で行こうかな
*   他の人の解答見てみた
    *   https://github.com/TORUS0818/leetcode/pull/9/files
    *   https://github.com/Mike0121/LeetCode/pull/42/files
*   step1 冒頭の None チェック、実は不要
*   tmp  というネーミングは流石によくないと思うので修正。
*   `reversed_head` とか `reversed_list` という変数名を見かけたが、ポインタを使う観点だとわかりにくいように感じる。`previous` の方が、実態に沿っていてよいのではと感じた。`previous` を使うと、`retrun previous` がちょっとわかりにくいかなとは思うけど。
*   1:00 かからずにさくっと書けた。

### step3

*   2 回目までやった。0:30 くらいで特に違和感なく書ける。


### step4

*   コメント集やレビューに再帰で解く方法について言及があるので、そちらをやってみる。
*   返り値一つのパターンでどうやるか考えるが、しばらく悩んでもわからんので LeetCode の解答眺めた
*   LeetCode にあるこれ書いてみたが、`p` が何なのかわかりにくい。
    *   よくよく考えていくと 1 -> 2 -> 3 の linked list だった場合、リストを進んでいって、3 に到達した時点で 3 の node を返し、以降 node 2、node 1 いずれの recursive call でも node 3 を返す -> 最終的に reversed list の head

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node is None or node.next is None:
            return node

        p = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return p
```

*   上記の GitHub も参照しただ、このあたりの Oda さんのコメントがわかりやすい
    *   https://github.com/goto-untrapped/Arai60/pull/27/files/14646ec0859dd9411e6983bf6c63e6f15a1f9f32#r1638693522
    *   https://discord.com/channels/1084280443945353267/1231966485610758196/1239417493211320382
    *   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.x5w37bodndgj
        *   TODO: コメント集のこのあたりもう少し掘ってみたい
*   正直再帰についてはまだ頭整理できていない。概念としてはわかるけど自分で書けと言われたときに違和感なくささっと書けるようにはなっていないので要連取
