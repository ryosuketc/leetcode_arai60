# 153. Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

## Comments

### step1

*   このあたりまで考えて 7:00 くらい。まとめきらなかったので
    *   l < mid -> search right?
    *   mid < r -> search left?
    *    すぐとなり？mid - 1 > mid だったら mid が最小？rotate していない場合の処理 (nums[0] が最小)

### step2

*   https://github.com/fuga-98/arai60/pull/42/files
*   https://github.com/hayashi-ay/leetcode/pull/45/files
    *   left を返すとなぜ答えになるのかわからない -> left == right だからか。
*   この 2 つを読んでみたが、いまいち納得できていないように思う
    *   https://github.com/olsen-blue/Arai60/pull/42/files
    *   https://github.com/hroc135/leetcode/pull/40/files
        *   *以下引用*
        *   昨日までの引き継ぎによると、どこかに最小値が存在しているらしい、探索対象区間[left, right]に対して、今日のmiddleの調査結果を加えて明日に向けて引き継ぎをする。
        *   middle = (left + right) // 2 が崖を越えた後か？越える前か？を今日調査する
            *   崖越えた後なら、middleは最小値になりうるし、middle - 1 以降の左側にも最小値が存在し得るので、[left, middle]を探索範囲にして引き継ぐ。
            *   崖越える前なら、 middleは最小値にならないが、middle + 1 以降の右側に最小値が存在し得るので、[middle + 1, right] にして引き継ぐ。
        *   最小値が存在し得る区間を絞っていき、探索範囲に1つだけものが残ったら終了する。(left == rightのとき) 結果的に nums[left]が最小値になる。
        *   初期値としては、[0, len(nums)-1]になる。まだ未探索の状態で、この範囲に最小値が存在しうる。
        *   middleの制約条件としては、[left, right - 1]の範囲でmiddleを選べば、探索範囲を小さくすることができる。
            *   (追記)下の方の Q1 の内容と関連するが、[0, 1]の状態で、middleを切り上げで計算すると、範囲が小さくならないのでmiddleは切り捨てで求める必要がある。
        *   *引用ここまで*
*   たとえば、概念だけ見た状態で、`step1.Solution1` を書いてみた。
    *   意識として、left, right は未探索の区間 (両端を含む)
    *   したがって、left は、それより左は条件を満たさない (最小値が存在しない) ことが保証されている区間、right はそれより右が条件を満たさないことが保証されている区間。
    *   確かにこれ (`nums[0] < nums[mid]`) だと、頭が最小だったとき、本来最小になる要素を除外してしまう (e.g. [1, 2, 3] のとき、1 (left) < 2 (mid) なので left = 0 + 1 となる)
        *   言われれれば気づくけど、これどうやって気づくんだろう。
        *   まあ適当なテストケースで気づくとは思うのだが、もうちょっと講師陣が期待しているであろう言葉の定義から理解するような方法で理解したいが…。
    *   `if nums[0] <= nums[mid]` はよく考えるとたしかに等号が必要。nums[0] が最小値でない = rotate はされている、と保証されている場合、[1, 2, 0] みたいなので、仮に mid=0 になったとすると、答えは必ず右側にあるはず。
https://github.com/seal-azarashi/leetcode/pull/39/files
    *   個々のケースを考えていくと、rotate されていなかったときの処理、等号を含める、のがそれぞれ必要だというのは理解できるのだが、最初の選定の段階で nums[0] と比較するのはなぜ筋がよくない (あとで edge case を追加しなければならない) のが理解したいのだが…
*   nums[-1] との比較 (`step1.Solution4`) だと rotate されていないときの処理は不要になる。左端 (0 や left) と比較するか、右端 (-1 や right) と比較するかで、なぜその差が出るのかいまいちうまく言語化できない。
*   https://github.com/Ryotaro25/leetcode_first60/pull/46#discussion_r1869993674
    *   追加質問に自分でも答えてみる (`step1.Solution4`)
    *   Q1.「2で割る処理がありますがこれは切り捨てでも切り上げでも構わないのでしょうか。」
        *   切り捨てである必要がある。right = mid にしているので、[0, 1] のような配列で切り上げると範囲が狭まらず無限ループする。
    *   Q2.「nums[middle] <= nums[right] とありますが、これは < でもいいですか。」
        *   よい。数字が重複しないことが保証されているので。
    *   Q3.「nums[right] は、nums.back() でもいいですか。」
        *   よい。というか今回はその実装を取った。mid が
            *   崖登り途中: まず、nums[-1] < nums[mid] がわかる。次に left, right は未探索の区間 (その間に最小値が必ず存在する区間) なので、right の方は必ず崖を越えているはず。したがって、nums[right] < nums[-1] < nums[mid]
            *   崖を越えた後: nums[mid] < nums[right] <= nums[-1]  
            *   以上から、どちらでも mid の状態を正しく判定できる。
    *   Q4.「right の初期値は nums.size() でもいいですか。」
        *   今回の実装ではだめ。left, right は両端を含む区間なので、nums[right]で範囲外になる。
    *   16 パターンでも答えてみる
        *   まず Q1 については常に切り捨てる必要がある (8/16)
        *   Q4 (nums.size()) にした場合は、Q3 (nums[right]) は範囲外なので NG (6/16)
        *   切り下げ、<、nums[-1], len(nums) の場合、left=0, mid=1, right=2 であれば、mid は最後の要素(-1) を示すことになり、`if nums[mid] < nums[-1]` を満たせずに left = mid + 1 になるが、left が範囲外。
            *   そもそも len(nums) を使うということは、right は「探索済み範囲の左端」(== ~right-1 までが未探索 == 最小値が存在する可能性のある範囲)。
                *   right = mid ということは、mid を探索済みにするということ。
            *   left については、定義にもよるが、「未探索の範囲の左端」を表すと考える。したがって left - 1 が探索済み。
                *   left = mid + 1 も、mid を探索済みにする処理。
            *   さて、この場合いずれも探索済みにする処理で、概ねどちらから探索済み範囲を伸ばしてもよいが、mid が最後の要素 (-1) である状況 (等号) では、left を動かす (mid + 1) と、mid (最後の要素) を通り過ぎて範囲外になる。当初の定義では、right は範囲外になる可能性があるが、left は必ず範囲内のはずで、その定義に矛盾する。したがって、等号は含める (右から探索済みにする) 必要がある。
    *   動くコード
        *   (切り下げ, <=, nums[right], len(nums) - 1)
        *   (切り下げ, <, nums[right], len(nums) - 1)
        *   (切り下げ, <=, nums[-1], len(nums) - 1) ＊
        *   (切り下げ, <, nums[-1], len(nums) - 1)
        *   (切り下げ, <=, nums[-1], len(nums))
*   https://github.com/olsen-blue/Arai60/pull/42/files#r1993168667
    *   > 「左側、つまり、条件を満たさないことが判明している左側の最大の場所」か「左側、つまり、条件を満たさないことが判明していない左側の最小の場所」かのどちらかを略して left と書いていることが多いんですよね。
*   https://github.com/hroc135/leetcode/pull/40/files#r1974926619
    *   > たとえば、「left とは、いままで見つかった false の位置の最大」で「right とは、いままで見つかった true の位置の最小」というのでもいいのです。そうすると、left, right が隣り合ったところで探索終了のはずです。


### step3

*   step2 で大分時間を使ったので一旦割愛。結構考え込む問題だったので、そのうち戻る。
