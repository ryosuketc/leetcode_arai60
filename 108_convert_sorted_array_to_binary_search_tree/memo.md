# 108. Convert Sorted Array to Binary Search Tree

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

## Comments

### step1

*   最初、nums の中の start_index, end_index を渡す再帰を考えた。ただ考えているうちに終了条件などがよくわからなくなって、初見から 5:00 くらい経過。
*   方針変更で、一旦 index を渡さず、nums のコピーを直接渡す形式にしてみた。9:00 で accepted (`Solution1`)

### step2

*   答えを見る前に index で書き直してみた。一度 nums のコピーで書いたベースがあったので 2:00 くらいで書き直せた (`Solution2`)。
    *   ただ、終了条件の `if end_index < start_index` を確認するのに、脳内でテストケースをゆっくり動かしてみる必要があって、1:00 くらい悩んだ (協会に = を含めるかどうか)。
    *   よく考えると、`end <= start` にしてしまうと、長さ 1 のリストに対して None を返してしまうので、その観点から境界を考えたほうがよかったかも。
    *   このあたり、境界を考えるの苦手かも。binary search のときに練習したい。
*   https://github.com/hayashi-ay/leetcode/pull/29/files
*   https://github.com/t0hsumi/leetcode/pull/24/files
*   上記含めいくつか見たが、今回はあまり解法に幅がなさそう。
*   どうでもいいことを思いついたが、mid pointer を求めるとき、ふつう (?) の言語だと int overflow を避けるために `low + (high - low) // 2` と書いたりするけど、Python だと int は無限なので必須ではないように思った。

### step3

*   2:30 -> 2:00 -> 2:00
*   len(nums) < 10^4 なので、再帰の深さは log10^4  = 4log10 なので 12 - 16 の間の数字くらい。recursion limit 的には全く問題がない。
