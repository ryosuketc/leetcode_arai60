# 121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Comments

### step1

*   4:00 くらいで解いた (`Solution`)。
*   1 回しか売買できないなら、折れ線グラフを書いたときに単に一番深い谷と高い山を比べればよい。谷が、山よりは前にある必要があるので、「それまで見た中での min」とする
*   逆に DP でどう解くのかよくわからんかった。
*   「そのインデックスまでの最大利益」みたいなリストを作るとは思うけど、最大履歴のリストの [i - 1] と [i] の関係はよくわからん。結局それまでの最低値は保持しないといけないのでは？
*  `for price in prices[1:]`、リストのコピーを作ることになるのは気に入らないので、避けたければ  `range(1, len(prices))` にするか、`for price in prices` で、1 番目の要素を含めたとしても動く。ただ、「choosing a different day in the future to sell that stock」というのを満たしていないような気分になり気持ち悪いのであえて 1 から走査した。

### step2

*   https://github.com/hayashi-ay/leetcode/pull/52/files
    *   なるほど、逆順で走査して max_price を保持しておく方法もあるか。今回の問題では使わないけど発想としては持っていてもいいかも。
*   https://github.com/fuga-98/arai60/pull/37/files#r2051630423
    *   ここ `assert type(prices) is list` している理由がわからない。for でループしているだけだから、`Sequence` なら何でもいいのでは？
    *   brute force な解き方もあるか
*   https://github.com/olsen-blue/Arai60/pull/37/files
    *   DP でもやはり最小値は保持している
    *   左右から見て最後に `zip` するやり方もあるのか。なるほど今回は使わなさそうだけど参考にはなる。
    *   以下引用。ただしループ内で分岐していて複雑なので、`step2.Solution` で書き直した。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices_from_left = [prices[0]] * len(prices)
        for i in range(1, len(prices)):
            if min_prices_from_left[i - 1] > prices[i]:
                min_prices_from_left[i] = prices[i]
            else:
                min_prices_from_left[i] = min_prices_from_left[i - 1]

        max_prices_from_right = [prices[-1]] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > max_prices_from_right[i + 1]:
                max_prices_from_right[i] = prices[i]
            else:
                max_prices_from_right[i] = max_prices_from_right[i + 1]

        max_profit = 0
        for min_price, max_price in zip(min_prices_from_left, max_prices_from_right):
            max_profit = max(max_profit, max_price - min_price)
        return max_profit
```

### step3

*   step1 のやり方が一番シンプルにできるのでそれで練習
