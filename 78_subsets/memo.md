# 78. Subsets

https://leetcode.com/problems/subsets/

## Comments

### step1

*   backtrack のカテゴリなんだから backtrack で解けるのかな、permutation と似た感じで行けそうなきもするけど、、とは思った。
*   が、手でやるときのイメージが、それぞれの数について、取る or 取らない の 2 択がある、というもので、それだったらビットを立てて探索していくのがいいよなあ、と考えた
    *   inner for loop で `bit` を改変しながら loop するのは (コードの動きとして問題ないことは革新があるのだが) 変数の値が途中で変わっていって、なんかちょっと気持ち悪いような気がしなくもない。でもこれがシンプルに書ける気はした。
    *   ビット全探索のとき、range の中身が `len(nums)` か `len(nums) - 1` かわからなくなったので小さいリストで確認した (長さ 1 のリストであれば `0b0` と `0b1` があればよいので、`1 << 1 = 2`、つまり `0, 1` を回せばよい)。
*   backtrack で解く方法も少し考えてみる。
    *   permutation だと、`len(nums) == len(perm)` になった時点で結果のリストに追加するが、subset だといつ追加すればよいかよくわからなかった。
    *   perm のときと同様に考えるなら、まず最初の数字について入れるか入れないかの 2 択があって、あとは残りの数字たちに対しても同様にやって残りの数を減らしていく。

### step2

*   https://github.com/fuga-98/arai60/pull/50/files
    *   ああ、stack (もしくは再帰の変数として) で何を管理すればよいかに気づくと簡単だった。特に何も見なくても 3:00 くらいで書けた。
    *   今構築中の subset と、nums で今注目している数字の index を管理していればよい
    *   この (`SolutionStack`) 書き方だと、`subset` 自体は mutate されない (subset 自体には append 等をしていない)
    *   stack がわかっていれば再帰に書き直すのはすぐ (`SolutionRecursion`)
*   https://github.com/olsen-blue/Arai60/pull/52/files#r2019033451
    *   これシンプルでかっこいいしロジックもわかるが本番で書けと言われたらちょっと嫌。脳内で動かしたときに緊張していると混乱しそうである
 
```python
all_subsets = [[]]
for num in nums:
    new_subsets = [ subset + [num] for subset in all_subsets ]
    all_subsets.extend(new_subsets)
return all_subsets
```

これは確かに backtrack っぽい。関数呼んで、append して、関数呼んで、もとに戻す (`pop`)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            all_subsets = []
            def traverse_nums(index, subset):
                if index == len(nums):
                    all_subsets.append(subset.copy())
                    return
                traverse_nums(index + 1, subset)
                subset.append(nums[index])
                traverse_nums(index + 1, subset)
                subset.pop()
            traverse_nums(0, [])
            return all_subsets

```

*   前回も結局構築中の perm をコピーして関数に渡したので backtrack っぽくない。結局 backtrack とはなんぞ、というのイマイチよくわかっていない。後ほど他の資料も見ておきたいが、汎化してどういうものか理解できていない気がする。

### step3

*   step1 で bit でスラスラ書けなかったので今回はそれを練習してみることにした。わかれば機械的に書ける。
*   bit を書き換えるのではなく `bit >> i` に落ち着いた。わかってればビット全探索書くのは一瞬。
