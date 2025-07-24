# 98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/description/

## Comments

### step1

*   7:00 で accept。
*   解き始めるとき以前の履歴が見えてしまって lower_bound, upper_bound で解けるのがわかってしまっていた…
*   node 数は 10^4 くらいなので、デフォルトの recursionlimit だと入らない可能性がある。ので、いきなり iterative DFS にした。
*   まあ別に BFS でも解ける。あまり差はないかな？
*   root is None のときに True なのか False なのかちょっと迷った。空の値をもらったときにどう処理するか？
    *   None 自体が falsy な値だから、False を返すことにしてみた
    *   この関数のユースケース、まあ何かの BST の入力があったとき前処理として弾いておきたい、みたいなニーズだと考えると、None はやはり invalid (False) であってほしいと思う
*   完全に余談だが、Truthy / Falsy が多分正しい。Truely / Falsely とか Truly / Falsly とかいつも間違えそうになる。
    *   https://developer.mozilla.org/en-US/docs/Glossary/Truthy
    *   https://developer.mozilla.org/en-US/docs/Glossary/Falsy

### step2

*   https://github.com/hayashi-ay/leetcode/pull/38/files
    *   inorder で increasing order になっているか見る手もあるか。
    *   morris in-order traversal も聞いたことはあるが一旦スルー
*   https://github.com/nittoco/leetcode/pull/35/files
*   https://github.com/Mike0121/LeetCode/pull/8/files
    *   inorder だとこっちがわかりやすいかな？
*   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.r5pdnx6retf4
    *   コメント集も軽く見る。
*   Python Generator
    *   https://discord.com/channels/1084280443945353267/1192736784354918470/1235116690661179465
    *   https://github.com/nittoco/leetcode/pull/35/files#r1739978684
    *   Generator 実はあまりわかってないし、`yield from` 始めて見た…
    *   https://docs.python.org/3.11/reference/expressions.html#yield-expressions
        *   https://qiita.com/keitakurita/items/5a31b902db6adfa45a70
            *   ラフな説明だが補足的に

```python
# oda さんの解答のコピペ
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_sort(node):
            if not node:
                return
            if node.left:
                yield from inorder_sort(node.left)
            yield node
            if node.right:
                yield from inorder_sort(node.right)

        prev_value = -inf
        for node in inorder_sort(root):
            if node.val <= prev_value:
                return False
            prev_value = node.val
        return True
```

*   step1 から、フォーマット的に書き直したいところは特段なかった。

### step3

*   今日は Tree, BT, BST のセクションが残り 1 問で解ききってしまいたいのと、step1 の時点でスムーズだったのでスキップ。
