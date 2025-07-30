# 776. Split BST

https://leetcode.com/problems/split-bst/

## Question

Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where the first subtree has nodes that are all smaller or equal to the target value, while the second subtree has all nodes that are greater than the target value. It is not necessarily the case that the tree contains a node with the value target.

Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.

Return an array of the two roots of the two subtrees in order.

Example 1:
Input: root = [4,2,6,1,3,5,7], target = 2
Output: [[2,1],[4,3,6,null,null,5,7]]

Example 2:
Input: root = [1], target = 1
Output: [[1],[]]
 
Constraints:

The number of nodes in the tree is in the range [1, 50].
0 <= Node.val, target <= 1000


## Comments

### step1

*   binary search tree なので、たとえば今の node が node.val <= target なら、node および node.left はいじる必要がなく、right をどこで切るかを考えればよい。node.val > target なら逆。
*   上の程度はぼんやり理解していたが、ぱっと再帰のコードに直せなかった。
*   5:00 ほど考えてよくわからんとなったので、ひとまず LeetCode の答えを見ることにした。
    *   step1 のコードは LeetCode の解答ベースのもの。そんなに読みやすくない。また今回だと、iterative にも書けるけど、やはり再帰で解くべき問題のように思う。

### step2

*   https://github.com/hayashi-ay/leetcode/pull/53/files
*   上記明確に言語化してコードも見た後だとさらっと書けた (`step2.Solution`)
*   step1、なぜか `bns` という変数に入れて index でアクセスしていたが、明らかに smaller, larger で unpack していたほうが可読性が高い
*   Iterative
    *   https://discord.com/channels/1084280443945353267/1237649827240742942/1327643938567360555
        *   ポインタを使っているのでこのあたりは Python だと再現しにくいかな？
    LeetCode Approach 2 見てみたけどわかりにくくないか (`step2.Solution2`)

### step3

*   `step2.Solution` の再帰をベースに練習
