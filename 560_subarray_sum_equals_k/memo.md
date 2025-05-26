# 560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/description/

## Comments

### step1

*   最初 subarray の定義がわからなくて問題文にある例が理解できなかった。
    *   **連続する**要素の配列 (長さが 1 も含む) ということだと理解
*   二重ループで回して、途中で sum_starting_from_i が k になったらそのループやめて…とか考えたけど、nums[i] はゼロ及び負の数もあるので、全走査しないと正しい答えが出ない。
*   TLE しそうだけど全走査したら答え出るよね、で書いた。案の定 TLE した (`Solution`)。
*   ここまでで 7:30 くらい。
*   subarray、というかそのループで和を求めているので、累積和使えばいいのかな？と思いつくけど、具体的な手順にまで落とし込めなかった。

### step2

*   LeetCode の答え (Approach2) 見て `Solution2` を実装した。
*   結局 TLE した。Java だと通るけど、Python だと TLE するっぽい (自分のコードが間違ってなければ)
*   というか `Solution`  も `Solution2` も O(N^2) で本質的に同じじゃない？ (`Solution2`  は累積和の配列を使っているけど、`Solution` は `sum_starting_from_i` の整数を使って O(1) spaace にしている)
    *   と思って LeetCode の Approach3 見たらその通りだった。
    *   つまり自分で考えた最初の解法 (`Solution`)、実際累積和の考え方を使っている (気づけば当たり前なんだけど、累積和といえば配列というバイアスがあった)
*   となると、O(N^2) の解法だと Python ではどう頑張っても TLE するのか…

*   https://github.com/potrue/leetcode/pull/16/files
*   https://github.com/Satorien/LeetCode/pull/16/files

### step3

*   
