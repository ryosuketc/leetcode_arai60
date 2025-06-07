# 105. Construct Binary Tree from Preorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

## Comments

### step1

*   3:00 くらい考えたけどまとめきらなかった。preorder[0] が root だというのはわかったけど、inorder をどう使えばいいかわからなかった。
*   LeetCode / NeetCode の解答見た。
*   ナイーブな解法は、`inorder.index(preorder[0])` で、inorder における root の位置を探索、またリストのスライスを渡す。
    *   このあたりは割と簡単に最適化を考えられた。前者は value -> index の map、後者はスライスではなくで left, right を渡す。
*   試しに解答を見ずに書いてみたら、`SolutionRuntimeError` のようになった。
    *   preorder のリスト内における index を管理せず、なぜか `root = TreeNode(preorder[left_index])` としてしまっている。
    *   これは「left_index が inorder リスト内での index である、ということを明確に言語化していなかったためだと思われる。
    *   一方で、「left_index, right_index は*両端を含む*探索範囲である」ということは言語化できていたので、`if left_index > right_index:` の部分は何も考えずに書けた。
*   `Soluton` が訂正版
    *   NeetCode だと、self.preorder_index とインスタンス変数 (__init__ ではなく `buildTree` 関数内で初期化) にしていたがこれは抵抗がある。インスタンス変数に、関数が呼ばれるたびに一時的な値みたいなものが格納されるのはどうなんだ。
    *   というわけで nonlocal を使う。使いたくなければ [1] のような mutable なものを参照渡し代わりにできるけど、まあ nonlocal が Python っぽいでしょう。

### step2

*   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.1rv0z8fm6lc3
    *   > たぶん、私は「え、そもそも、Preorder と Inorder で再現できるだけの情報あるのかよ。異なる2つの木で Preorder と Inorder が同じになっちゃうような場合って本当にないの。」みたいな疑問をもって、それを解消に行く気がします。この疑問を解消しておくと、どういう作業をしたら元の木が決められるかが分かると思います。
    *   > 「自分で手作業でできる」ようにして「人に手作業でできるように説明をする」というプロセスを踏むと、明らかに無駄なところは気がつくように思うんですよね。しかし、それはともかくそうだとしても、遅くてもいいから動くものを作ってしまうのは一つです。そちらのほうが簡単そうならば。
*   preorder による構築
    *   https://discord.com/channels/1084280443945353267/1247673286503039020/1300957769477918791
        *   1 つ 1 つの行が何をやっているかはわかる。全体としてやりたいこともなんとなくわかる気もするが微妙。スタックの役割をいまいち言語化できていない。
    *   https://github.com/nittoco/leetcode/pull/37#discussion_r1831463376
        *   考え方の補足
    *   うーん、5 mins くらい考えたが、ちょっとわかるようなわからんような。一旦先に進む
*   inorder による構築
    *   https://discord.com/channels/1084280443945353267/1247673286503039020/1300957861614063616
        *   パット見、preorder よりさらにわからない。`gather_descendants` ってなんだ
    *   https://github.com/fuga-98/arai60/pull/29#discussion_r2020242408
        *   まあ概念としてはわかるような気もする 
*   総じて、preorder / inorder による構築はまだぼんやりとしか理解できていない。どこかで戻ってきたいとは思うけど、なんでこういう複雑な (?) のを思いつけるんだろう。
    *   今の自分だと、仮にぼんやりと思いついたとしてもアルゴリズムとして整理して実装できる気がしない…
    *   私の step1 (LeetCode / NeetCode ベース) はまだ思いついて書ける気がするが。
*   他の人の実装
    *   https://github.com/hayashi-ay/leetcode/pull/43/files
        *   概ね私の step1 と同じ実装。変数名がより整理されている。
*   結局 step1 について変数名を少し整理しただけにとどめた (step1)
    *   `value_to_inorder_index` の構築を関数に切り出すか一瞬考えたけど overkill だなという印象。短く書きたいならリスト内包表記もいい。

### step3

*   初回は typo とか、TreeNode を作り忘れるとかあまり馴染んでない。何回か submit してはエラー直す感じだったので本来はノーカウント
*   2 回目 (実質的初回) は 6:00。結構スムーズだった。
*   3 回目 (実質的 2 回目) 5:30
*   本来もう 1 回やりたいのだが時間切れ。
