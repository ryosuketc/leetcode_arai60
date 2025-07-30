# 198. House Robber

https://leetcode.com/problems/house-robber/

## Comments

### step1

*   9:30 で `SolutionWA`
*   有名な問題だと思うけどかなりうろ覚えだった。なんとなく前 2 つを参照して DP できるというのは覚えていたが
*   なんとなくこれでいけるんじゃないか、くらいの確信度で `SolutionWA` 書いてみたがまあ WA。
*   ある程度時間経っていたので答え見た。
    *   ああ、なるほど、`SolutionWA` で、dp のリスト (`max_money_rob_house`) を、「そのインデックスの家に盗みに入った場合の最大額」、と定義していたが、正しくは、「そのインデックスまでの最大額」なのか。
*   O(1) space で解く、再帰で解くそれぞれあると思う

### step2

*   `step1.Solution` のコード、`not nums` のときを考慮できてない

```python
        if len(nums) <= 1:
            return nums[0]
```

*   https://github.com/Mike0121/LeetCode/pull/47/files
    *   上記追加しつつ `step1.Solution` をベースに space O(1) にする -> `step2.Solution1`
    *   バリエーションとして、previous を両方ゼロで初期化して、nums を全部 (i = 2 以降ではなく) 走査することもできる -> `step2.Solution2`
    *   上記 PR では配列の前から再帰するパターンを書いている。`if i >= len(nums): return 0` と、nums を超えたときにゼロを返すのがなんか気持ち悪い木がしたので、配列の後ろから再帰するパターン (`Solution3`) で書いた。
    *   thread safety に関するコメント参考になった: https://github.com/Mike0121/LeetCode/pull/47/files#r1799964450
*   https://github.com/hroc135/leetcode/pull/33#discussion_r1899009212
    *   計算量の話難しい。まあなんとなくはわかるんだが面接でふと出てこない気がする。
    *   一応ここでも言及はしている: https://github.com/ryosuketc/leetcode_arai60/pull/46/files
    *   `skippedLast` とか `robbedLast` とかはそれなりにいいかもしれない
*   https://github.com/hayashi-ay/leetcode/pull/48/files

### step3

*   DP が一番素直な感じがしたので DP で。step2 で色々書いていてすんなり書けたので溶き直し省略
