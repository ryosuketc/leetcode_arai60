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
    *   left を返すとなぜ答えになるのかわからない

*   https://github.com/olsen-blue/Arai60/pull/42/files
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


### step3

*   
