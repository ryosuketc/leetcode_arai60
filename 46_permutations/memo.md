# 46. Permutations

https://leetcode.com/problems/permutations/

## Comments

### step1

*   Backtrack の問題だとはわかっているがとりあえず `itertools` を使いたくなった
    *   https://docs.python.org/3/library/itertools.html
*   たとえば `[1, 2, 3]` が来たとき、一個数字を選んで先頭に置く、残りをまた permutation を求める、という手作業のイメージで書こうとした。15 分くらい悩んだので断念。
    *   最初 `1` を取る。`[2, 3]` の順列を取る。構築中の順列は `[1]`
        *   `2` を取る。[3] の順列を取る。構築中の順列は `[1, 2]`
            *   `3` を取る。[] の順列を取る (残りの数字がなくなったのでおわり)。構築中の順列は `[1, 2, 3]`
        *   (`[2, 3]` の順列を取るところに戻って) `3` を取る。[2] の順列を取る。構築中の順列は `[1, 3]`
            *   `2` を取る。[] の順列を取る (残りの数字がなくなったのでおわり)。構築中の順列は `[1, 3, 2]`
    *   結局構築中の順列をうまく管理できなくて書けなかった気がする

### step2

*   https://discord.com/channels/1084280443945353267/1233603535862628432/1238727359280971796
    *   `SolutionStack`: 上のを Python で書いてみた。
    *   `SolutionRecursion`: 再帰に直した。`SolutionLeetCode` とほぼ同じ形になった。


```python
                new_perm = perm + [num]
                perms_in_construction.append(new_perm)
```

こう書くこともできる。こっちのほうがリストのコピーが発生しないからちょっと効率がよいかも。ただ `1 <= nums.length <= 6
` なのでまあどっちでも。

```python
                perm.append(num)
                permute_helper(perm)
                perm.pop()
```

*   https://discord.com/channels/1084280443945353267/1233603535862628432/1238878881910493255
    *   自分が step1 でやろうとしたのはこれか
    *   `SolutionNumsLeft`: 上記をベースに書き直した
    *   これ書き直して気づいたけど、`step1.SolutionWA` 結局リストのコピーを渡せばよかっただけ…
        *   `SolutionStep1Fixed` で直した。
*   多分出元は NeetCode だと思うけど一番 in-place で効率良さそうなのがこれ。
    *   backtrack もインデックスだけした使わず、swap しながら順列を作る
    *   ただ、あんまり手作業でこれやる感覚はないかも。
*   TODO: まだ計算量の話はちゃんと理解できていない
    *   https://github.com/Ryotaro25/leetcode_first60/pull/54#discussion_r1986035628
*   TODO: Backtrack
    *   なんだかんだ backtrack はまだよくわかってない。リストに追加して、backtrack して、戻して、という形式で覚えてはいるけど、みたいな程度
    *   https://github.com/fuga-98/arai60/pull/49/files
    *   https://www.cc.kyoto-su.ac.jp/~yamada/ap/backtrack.html

### step3

*   nums から 1 つ選んで、残っている nums を渡していくやり方が、自分が一番最初に思いついた手作業のやり方で馴染みやすいのでその方法で練習した
