# 209. Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum/

## Comments

### step1

*   12:20 くらいで `SolutionWA` を書いた。
    *   ただし最初の submit で、inf のままのとき 0 を返すというのを忘れていた
*   sliding window を使うという前提があれば割に簡単だった。
*   nums の要素が positive であるという前提なので、ターゲットより大きくなった時点で左を縮めていけばよい。
*   ただ `SolutionWA` がなぜ WA になるのかテストケースを見てもよくわからなくて、過去の自分の解答を見てようやく気づいた
    *   >  return the minimal length of a subarray whose sum is **greater than or equal to target**
    *   ターゲットが = になるものだと思っていた
    *   修正 `Solution`

### step2

*   https://github.com/olsen-blue/Arai60/pull/50/files
    *   解法としてはほぼ同じ方向性
*   bisect / 二分探索を使う方法
    *   この方法は全く頭になかった。subarray の和だから累積和を使うことはできるなーと思ったけど (O(n^2))。
    *   https://github.com/hayashi-ay/leetcode/pull/51/files
    *   https://github.com/Mike0121/LeetCode/pull/22/files
    *   累積和の配列は単調増加なので、この配列に対しては binary search ができる。
    *   ただこのやり方、step1 とは逆で、左を動かしていって、bisect で右側を見つける、という処理になる
        *   累積和の配列に対して、現在の累積和 (左) + target を挿入できる位置を探す。つまり subarray の和が target より僅かに大きくなる (もしくはイコール) 挿入位置を探す
        *   bisect_leftの返り値 (挿入位置) がリストの最後 (`len(nums)`) になるときは、それ以上左を動かしても累積が増えるだけなので打ち切る
    *   ここらへんまで見て空で書いてみた
        *   間違えて `from collections import accumurate` と書いた
        *   正しくは`from itertools import accumulate`
        *   この解法だと、bisect_left の返り値は `prefix_sums[left] + target` を挿入できる位置なので、`right - left` が正しい (vs. `right - left + 1`。ここでいう right より 1 index 分先に進んでいる)
        *   ちなみにこの解法だと `from_index` とか `target_index` という変数名でもいいのだが、step1 との対比のため left, right を継続して使用した

### step3

*   sliding window の感覚的に、右を順次動かしながら、左を縮めるほうが感覚にあっている気がする
