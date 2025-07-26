# 253. Meeting Rooms II

https://leetcode.com/problems/meeting-rooms-ii/

## Problem

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

## Comments

### step1

*   11:30 くらいで AC
*   図示すると、数直線上でダブっている最大個数分の部屋が必要 -> このイメージからうまくコードにはできなかった。
*   愚直にやると、今占有中の部屋のリストに start_time, end_time を突っ込んでいき、次を処理するときに、占有中の部屋のリストを全てなめて削除できるものを探すとか？
*   なんとなく sliding window 的なものが頭に浮かんだ。
    *   この解き方で解けることはサンプルケースで確認してコードを書き始めたが、逆にこれ以外に明確に解き方が思い浮かぶものがなかった。
    *   一発書きしてみて、問題なさそうだったので submit したら AC

### step2

*   step1 でコメントしたが、`# When the same time is given, end should be processed first.` というのは割とすぐに思いついていた。なので、END < START になるように定義するのは必要。逆にすると WA になる (余分に 1 部屋必要になるので)。
    *   このエッジケースをちゃんと考えていたのは良かった気がする。
*   2022 年にこんなコード書いていたらしい (`Solution1`)
    *   e_ptr とか変数名いけてないな。今なら `end_index` とかにするかなあ
    *   まあ確かにこれ解けるな。部屋を増やしながらstart を走査して、end <= start であれば部屋を減らして e_ptr を進める
    *   `Solution1_1` で書き直してみた。
        *   これよく考えると、`num_ongoing_meetings` しか管理していなくて、そのままそれを return しているが、必要な部屋の最大数、みたいなのって track してなくていいんだっけ？
*   https://github.com/nittoco/leetcode/pull/45/files
    *   `functools.total_ordering` しらなかった
        *   https://docs.python.org/ja/3.13/library/functools.html#functools.total_ordering
    *   私の step1 は最後に sort したが、heap に入れる手もあるか。思いついていなかった。
*   https://github.com/olsen-blue/Arai60/pull/57/files
    *   https://github.com/olsen-blue/Arai60/pull/57#discussion_r2027474114
        *   > まあ、これでもいいんですが、私、この問題を手で解くとして、解法の取りうる範囲の数字を全部挙げはじめたら結構驚くと思うんですよね。浮動小数点だったらこのままでは駄目ですよね。
        *   > ここの疎な部分を減らすのは座標圧縮に相当するのですが、しかし、座標圧縮した結果の解法がいきなりでてきませんかね。
        *   > MAX_RANGE 使っていない解法をちょっと読み直してみませんか。
        *   実は取りうる時間範囲全部走査するの step1 で一瞬思って、処理が膨大でかつ無駄が多すぎるのでやめた…
    *   座標圧縮
        *   https://qiita.com/mm-saito-1204/items/7ee43bc83c9bc766535b
        *   前問でも多少触れているがまだあまりわかっていない
            *   https://github.com/ryosuketc/leetcode_arai60/pull/55/files
            *   とりあえず今回のコード自体は意味はわかる。時間軸全部を操作するのではなく、rank (unique で連続の数値) に対応する index の数値を増減させていく。
    *   tuple の 2 つめの要素 (私のコードだと `time_type`)、これ自体に +1 (start) or -1 (end) を入れるとそれ自体を足したり引いたりできる。
    *   `Solution2` で書いてみた。うーん、なんかわかりにくい。type で分けるほうが好みかも。
*   https://github.com/hayashi-ay/leetcode/pull/62/files
    *   `Solution3`: 5th, 6th の heap を使った書き方、あまり考えていなかったがこれはこれできれい。
        *   本質的には、`Solution1`, `Solution1_1` と同じ解法。ただ heap で管理している方がわかりやすいかな。


### step3

*   step2 でいろいろな解法を書いて割と再現性もあったので、時間もなさそうだし今回は省略。step1 の解答をベースに変数名等だけきれいにした。
