# 252. Meeting Rooms

https://leetcode.com/problems/meeting-rooms/

## Problem

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

## Comments

### step1

*   sort せずに解こうとするなら、全ての組み合わせをチェックすればよく O(n^2) で解ける。
*   sort の方が O(nlogn) なので、sort したほうがよい
    *   もしかしたら小さいリストだと sort しなくても O(n^2) の方が速いケースはあるだろうか？？
*   8:30 くらいまでで `Solution1`, `Solution2` 書いた (AC)
    *   `[[0,30],[5,10],[15,20]]` のような、最初の end_time がやたら長いやつ (その後 i=2 なんかでも、まだ終わっていないパターン) を handle しようとして `previous_end_time = max(previous_end_time, end_time)` とした。
    *   ただよく考えると今回は全ミーティングに出られるか判定すればよく、出られないときは return False するので、max を取る必要は特にない (単に前の要素にアクセスすればよい) -> `Solution2`
*   今回だと、`len(intervals) == 0` は特別か使いしなくてもよい (True を返すので、for ループが実行されないだけ)。1 の場合はどうだろう？前のミーティングにアクセスするので、特別扱いする必要はありそうだが…？

### step2

*   https://github.com/hayashi-ay/leetcode/pull/59/files
    *   なるほど、prev_end を 0 あたりで初期化すれば動くか。
    *   heap 使うのは思いついていなかった。
*   https://github.com/olsen-blue/Arai60/pull/56/files
    *   冒頭の解法、累積和というよりは、文字列のカウントに似た印象。全パターンを網羅できる長さの配列を用意し、対応する index に +-1 していく。文字列が a-z だと仮定したとき、[0] * 26 の配列を用意すればいいのと同じ。
        *   確かにこれだと sort しなくていいから、space complexity の制約がゆるいならありか。
        *   ただ後半でコメントあるように整数以外の入力については動かない。座標圧縮というのもあるらしい。
            *   https://qiita.com/mm-saito-1204/items/7ee43bc83c9bc766535b
                *   要素が重複しているなら座標圧縮によって節約できるメモリは多いけど、あまり重複がないならさほどメリットはない？
        *   最後の解答、end_time で sort してるのか。今回はどちらでもよいと思うけど。
    *   step1 でやったみたいなの、区間スケジューリング問題というのか。へー。確かに競プロの用語なのかな？そっちはあまりやらないのでよくわからんけど。
        *   https://qiita.com/uniTM/items/0dbd7ec962186c005c08

### step3

*   step2 と同じ。変数名や条件分岐含めてこれが一番シンプルできれいかなと思った。
