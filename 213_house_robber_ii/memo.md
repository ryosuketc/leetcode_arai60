# 213. House Robber II

https://leetcode.com/problems/house-robber-ii/

## Comments

### step1

*   house robber と関連問題なので連続で解いてみる
*   cycle というか円になっているやつというのは覚えていたけど、解き方はいまいち覚えてなかった。
*   でも house robber と基本の考え方は同じで、リストの末尾、最初の処理だけ変わると思った。
*   どうやればいいかしばらく考えた。あまりシミュレーションしっかりできてないけど、house robber を 2 回やれば解けそうな気がした。
    *   とりあえず書いてみた。AC。でもこれは前解いたとき (2 年前くらい？) のをなんとなく覚えてたのかも。
    *   inner function の引数名は別に nums でいいんだけど、外側のを override するのが嫌 (階層化されたスコープで同じ名前だとちょっと読む負荷が高まる気がする) なので別の変数名にした

### step2

*   https://github.com/hayashi-ay/leetcode/pull/50/files
    *   基本的な考えは同じ解き方だが、こんな感じで初期化して dp list を 2 つ保持すれば一回のループでも解けるか。

```python
        max_amount_rob_first[0] = nums[0]
        max_amount_rob_first[1] = nums[0]
        max_amount_not_rob_first[1] = nums[1]
```
*   contd.
    *   ただ再利用のような観点で言うと、cycle になっていない rob を関数化して 2 回使っている解法のほうがきれいだと感じる。
    *   一応 space O(1) でも書いた
*   https://github.com/Fuminiton/LeetCode/pull/36/files
*   https://github.com/fuga-98/arai60/pull/36/files
    *   再帰について詳しい


### step3

*   house robber と同じコードなので練習は控えめ。素直な DP で練習した。
