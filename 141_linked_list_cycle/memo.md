# 141. Linked List Cycle

## Link
https://leetcode.com/problems/linked-list-cycle/description/

## Comments

### step1

*   通った Linked list を hashset に記録するのが一番簡単に解けそう
*   fast, slow ポインタを使うと解けるのは知識として知っていた
*   最初 `head.next` の None チェックをしていた (head が None になるのを考慮していなかった)
*   最初 `slow, fast = head, head` で初期化していたが、ループの条件を `slow != fast` にするためにずらした。
*   next の None 判定をするとき (ループがないとき) の分岐条件をどうするかに 2,3 分悩んでしまった (最初 fast.next のみチェックしていた) のでひとまず leetcode の答え見た (もうちょっと悩んだほうが良かった気がする)

### step2

*   discord で同じ問題の Python 回答を数個見たが、とりわけなにか追加したい要素は見つけられなかった
*   slow, fast を両方 head に assign するとき、`slow = fast = head` にするか `slow, fast = head, head` にするか少し迷った。今回は同じオブジェクトだから差分はなし。もちろん `a = b = []` と `a, b = [], []` だと違うけど…

### step3
*   2 回くらい試したが step1 で書いたコードは特に何も見なくても書けた
*   何回書いても同じになるので step2.py, step3.py は省略しようと思っていたが、step1 でループの条件を迷ってうまく書けなかったのはこれだった (https://algo.monster/liteproblems/141 変数名だけ変えたのが下記)。fast と fast.next の None をチェックすればよかった。
    *   こっちだと slow, fast はどちらも head に assign する。もしくは冒頭に head の None チェックをする。slow, fast 系の問題、最初に両方 head にすべきか head と head.next にすべきかいつもちょっと迷う。
    *   全体的にはこちらのほうがシンプルで好きなんだけど、理由についてはいまいちうまく言語化できていない。
    *   下記 (サイトにあったコード) だと `while fast ...` にしているけど、None check は explicit にしたくなる
        *   https://google.github.io/styleguide/pyguide.html#214-truefalse-evaluations

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # if head is None:
        #     return False 
        # slow, fast = head, head.next
        slow =  fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
          
            if slow == fast:
                return True

        return False
```