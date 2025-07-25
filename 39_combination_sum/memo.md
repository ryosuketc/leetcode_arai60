# 39. Combination Sum

https://leetcode.com/problems/combination-sum/

## Comments

### step1

*   8:30 くらいで `SolutionWA1`
*   引き継ぎとして `total, combination, index` の 3 つが必要そうだと思った
*   `[2,3,6,7]`, `target=7` について
    *   Expected: `[[2,2,3],[7]]`
    *   Actual: `[[2,2,3],[2,2,3],[2,2,3],[2,2,3],[7],[7]]`
*   というようにダブりが発生してしまう
*   まず `if index >= len(candidates):`, `if total > target:` は追加するより先にチェックする必要がある (`SolutionWA2`)
    *   Actual: `[[2,2,3],[2,2,3],[2,2,3],[2,2,3],[7]]` に。
    *   追加されるときの呼び出しはこんな感じ。

```
total=7, combination=[2, 2, 3], index=1
total=7, combination=[2, 2, 3], index=2
total=7, combination=[2, 2, 3], index=1
total=7, combination=[2, 2, 3], index=2
total=7, combination=[7], index=3
```

*   こういうダブりが出るの、submit 前の脳内デバッガで走らせたときは気付けなかった。ちょっとなんとなく書いたというか、終了条件さえあればちゃんと終わるだろう、くらいのゆるい感じで submit してしまった。
*   解決策はよくわからない。もちろん set で管理すればできるけど…


### step2

*   https://github.com/nittoco/leetcode/pull/25/files
*   https://github.com/fuga-98/arai60/pull/51/files
    *   再帰の解答 (下記) を眺めて、`2. Use the current number and move to the next number` がダブりの原因らしい。
    *   実際当該箇所をコメントアウトするだけで AC
    *   まあそれもそうか。同じ数字を何度もつかってよいので、以下だけで全シナリオがカバーできる。使って同じ数字にとどまる場合、使わずにスキップする場合 (使って次の数字に行くパターンは再帰で 「1 が何度か呼ばれた後に 3 が呼ばれる」というのでカバーできる)。
        *   `1. Use the current number and stays in the same number`
        *   `3. Skip the current number`

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(index, total, combo):
            if index >= len(candidates):
                return
            if total > target:
                return
            if total == target:
                result.append(combo)
                return
            helper(index+1, total, combo)
            added_total = total + candidates[index]
            added_combo = combo + [candidates[index]]
            helper(index, added_total, added_combo)
        helper(0, 0, [])
        return result
```
*   contd.
    *   副作用のない再帰、なるほどこうやればk helper の外部で値を保存していなくても再帰関数から直接返せるのか。
    *   計算量はこういう感じらしい。全然わからん。なるほど。
        *   https://github.com/fuga-98/arai60/pull/51/files#r2105014469
*   https://github.com/olsen-blue/Arai60/pull/53#discussion_r2021984357
    *   確かに気持ちはわかるがちょっと笑えた
*   DP のパターンがあるようだ
    *   今日ちょっと時間がないので TODO に入れておこう…
    *   DP はやはり苦手意識がある。特に 2D-DP
*   DP や、あるいは for ループで書いているのもあって、現時点ではいまいち理解しきれていない。もうちょと他の人の解答を読み込んでいきたい
    *   https://github.com/olsen-blue/Arai60/pull/54/files
    *   https://github.com/fuga-98/arai60/pull/51/files
    *   https://github.com/nittoco/leetcode/pull/25/files

### step3

*   なんとなく再帰が一番自然な感覚な気がした
