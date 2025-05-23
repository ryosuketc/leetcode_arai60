# 703. Kth Largest Element in a Stream

https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

## Comments

### step1

*   ぱっと思いつくのは、リストを毎回 sort しておいて、適宜一番小さい item を pop していく
    *   init で O(NlogN)、add のときは insert する場所を探すから O(N) (or binary search するなら O(logN))
*   4 分くらい考えたけど、ちょっと混乱してきたので一旦答え見た
    *   なぜか min heap と max heap を用意して…みたいなのにとらわれた。後で考えるとそれは median 求めるやつの話だった。
*   結局、それまでに見たもののうち、最大の k 個キープしておいて、間に割り込む数 (つまり今の min heap の最小値よりも大きいもの) が出たら小さいものから捨てていく。
    *   なので min heap がよい (add は O(logN))
*   `heapq` 久々だったのでインターフェイス忘れかけてた
    *   TODO: https://docs.python.org/3/library/heapq.html
    *   そういえば Python の heap は min heap で、max heap として使う場合は入れる値を negate する手があるけど、producton でそれやったらちょっと？ってなりそうな気もする？
    *   Python で (prod で) max heap 使いたいときどうするんだろう。まあ heapq の薄い wrapper でも書けばいいんだろうか。 


### step2

*   いくつか眺めてみる
    *   https://github.com/TORUS0818/leetcode/pull/10/files
    *   https://github.com/Mike0121/LeetCode/pull/19/files
*   heap は必要に応じて自前で実装できるようにすべきか。数年以上前に DSA 系のコースで色々見たけどもう忘れたので…
*   たしかに add の、この行不要ではある

```python
if len(self.min_heap) < self.k or self.min_heap[0] < val:
```

*   割とシンプルに書けはしたが、1 question / day を維持するために、ここの問題の掘り方が浅くなってるかも。6 questions / week くらいで、buffer 作ってもいいかも。

### step3

*   1:30 -> 1:25 -> 1:30

