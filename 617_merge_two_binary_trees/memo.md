# 617. Merge Two Binary Trees

https://leetcode.com/problems/merge-two-binary-trees/description/

## Comments

### step1

*   最初 iterative DFS (`nodes_pairs = [(root1, root2)]` のような stack) で書こうとしたが、結局、今の node だけに注目していると、どの node の child なのか管理しないといけない気がして、再帰に方針変更
    *   limit が 2000 なので、まあ recursionlimit を変更するかは環境次第か
*   10:00 くらいで `Solution1` まで書いてみた。`new_node.left = merge_trees_helper(node1.left, node2.left)` のあたりで None に left / right をやって runtime error になった。この時点で、node1 が None、node2 が None、両方 None でないの 3 パターンがあり、これごとに条件分岐するの非常に面倒だなと思う
*   get_left もしくは三項演算子を使って node1_left みたいなのを定義はできるが、node1_left, node2_left. node1_right, node2_right すべてやるの面倒だな…
*   ここまでで 13:00 以上経過していたので一旦打ち切り
*   -> あとで一応ベタ書きしてみた…これはひどい (`Solution2`)。二分木ではなく四分木だったらもっとひどい。

### step2

*   https://github.com/hayashi-ay/leetcode/pull/12/files
    *   なるほど既存の木を編集していく想定だった？
    *   ああそうか片方が None のときは merge する必要がなく、もう片方を返せばいいだけか。
    *   そうすると merge するのは、いずれも None でないケースに限定されるので書きやすい
    *   ここなんとなく書きたくはなるが確かに `if root1 is None` でカバーされているから不要ではある
    *   `çopy.deepcopy` で非破壊的にできる。コピーに時間かかるがいいかは微妙だけど。

```python
        if root1 is None and root2 is None:
            return None
```

*   https://github.com/nittoco/leetcode/pull/30/files#r1693985989
    *   これでシンプルに書ける
*   https://github.com/nittoco/leetcode/pull/30/files#r1693945861
    *   仕事を押し付ける、押し付けないの議論がよく理解できていないのでまた読む。

### step3

*   2:00 前後。とりあえずこれが一番シンプルな解法だと思われる。
*   ここは却って読みにくい気もするので、あまり使わないほうがいいかな。

```python
        # if root1 is None or root2 is None:
        #     return root1 or root2
```
