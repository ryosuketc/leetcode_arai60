# 322. Coin Change

https://leetcode.com/problems/coin-change/

## Comments

### step1

*   DP でも行けそうだが、前問の word break で、残りの string を減らしていくアプローチがしっくりきていたので、残り金額を減らしていくrecursion なら素直に解けるかなと考える。
    *   引数に amount だけを取る形にしないと cache が大きくなりすぎるかなと思ったが、コインの最小枚数を求めるので、その amount に至るのに必要だったコインの枚数も引き継ぐほうが簡単かなと考えて書いてみた。
    *   `Solution1MLE` を書くが # Memory Limite Exceeded

### step2

*   LeetCode の `Approach 2 (Dynamic programming - Top down) [Accepted]` の解答が自分のアプローチに近そうだったのでまず見てみた。
    *   軽く見て再現しようとしたが WA (`Solution1WA`, `Solution2WA`)
        *   `Solution1WA`: `amount < coin` のときはそもそも関数を呼ばない
        *   `Solution2WA`: `amount < coin` のときは None を返す
            *   `isinf(min_coins):` のときは -1 を返すので、`coin_change_helper(1) == -1` となり、`coin_change_helper(3)` のときに `min_coins` がアップデートされてしまう。
        *   ので、None ではなく -1 を返す必要がある (`Solution3AC`)
*   dp list を使う方法でも書いてみる
    *   `Solution4AC`
    *   こちらの方が条件分岐少なくてきれいだろうか。
    *   内側のループの変数名 `i` でよいのかは微妙。
    *   内側のループで、i の初期値を coin とするのがポイントかな。
*   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.ic8466had15a
    *   https://github.com/Yoshiki-Iwasa/Arai60/pull/54#discussion_r1739985190
        *   > 1つの変数に、最低何枚で作れるかと、そもそも作れるかのふたつの意味を持たせようとしているのが、条件分岐を作っているので、そもそも作れるかを別の配列で持つのは一つの方法です。場合によってはクラスを作ってしまうのも一つでしょう。それはそれでややこしくなったりするので状況次第ですが。
    *   https://github.com/TORUS0818/leetcode/pull/42#discussion_r1904039471
        *   -1 の扱いが気に入らなかったので Generator 使うのは考えてみました。
        *   これは思いつかなかった。まだ generator の使い方・使い所があやふや。

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def coin_change_helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            def possible_changes():
                for coin in coins:
                    num_coins = coin_change_helper(amount - coin)
                    if num_coins == -1:
                        continue
                    yield num_coins + 1
            return min(possible_changes(), default=-1)
        return coin_change_helper(amount)
```

*   https://github.com/TORUS0818/leetcode/pull/42/files
    *   BFS で解くやり方もあるか。コンセプトとしてありそうだとは思っていたが、どう実装するかまで考えていなかった。review コメントはあるものの、amount_and_num_coins の 2 要素を入れたキューはわかりやすいと感じた。
    *   coins のソートについては考えていなかった。
    *   keyword only は知っていたが、`/` で positional only にできるのは知らなかった。
    *   TODO: ここにある解き方、全部はしっかり理解できていないのでまた今度掘りたい。
*   https://github.com/hayashi-ay/leetcode/pull/68/files
    *   この例のように、amount のループを外側に持ってきたほうが直感的な操作とは合っていそう。DP テーブルの添字自体も、amount を基準にしているので、amount=1 から走査する。
*   https://github.com/fuga-98/arai60/pull/40/files
    *   > 自分なら
    *   > amount = 10^4
    *   > coins = [1, 2, ..., 12]
    *   > として、ある金額から 12 通りの分岐があるため、 10000^12 または数桁小さいと見積もると思います。*
    *   TODO: 全部はしっかり理解できていないので今度改めて見る。
*   https://github.com/olsen-blue/Arai60/pull/40/files
    *   TODO: 全部はしっかり理解できていないので今度改めて見る。

### step3

*   hayashi-ay さんの解き方ベースのものが一番手馴染みはよかった。
*   Generator を使った書き方もきれいだと思うので、慣れていきたいがまだ使い所が掴めてないかも。
