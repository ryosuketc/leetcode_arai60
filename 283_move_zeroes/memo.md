# 283. Move Zeroes

https://leetcode.com/problems/move-zeroes/

## Comments

### step1

*   in-place でなくてよいなら、最初の pass で non zero elements を append して、残り len(nums) に到達するまで zero を追加すればよい。
*   最初 zero_index を後ろから始める `Solution1WA` を書いた。ただ脳内で動かしてみてこれだと order が維持されないことに気づいた (開始から 6:00 くらい)。
*   zero_index を前から始めたらどうなるんだっけ？と表 `Solution2WA`
    *   これだと 0 が最後ではなく最初に移動する
*   ハマって 10 分くらい考え込んでしまったので答え見た。
    *   あ、`if num != 0` にすればいいだけだった。
    *   後で考えると、zero_index を最初から始めることにしたときに、その意味合いをちゃんと考えていなかった。
    *   `zero_index=0` から始めて `num != 0` で動かす場合、「0 がある最初の index」となるので、順次 swap すれば解ける。
    *   `zero_index=0` から始めて `num == 0` で動かす場合、「0 でない要素がある最初の index」となるので、順次 swap すると 0 が最初に移動する。
        *   この辺の理解、割と間違っている気がする (step2 / step3 で検討)

### step2

*   https://github.com/fhiyo/leetcode/pull/54/files
    *   zero_index という名前、というかその解釈、割と間違っているかも。`nonzero_length` とか `last_nonzero_index` とか？？
        *   結局 `num != 0` のときに動かすので、step1 のコメントは間違っていて、「それより左はゼロが削除されていますよ」くらいの意味合いかも (ゼロが削除された文字列の長さ)。
            *   後で関連コメントも見つけた: https://discord.com/channels/1084280443945353267/1201211204547383386/1230568276690468917
                *   > first_zero_index というか、私の感覚は、ゼロが削除された文字列の長さですね。
        *   いやまあ「0 がある最初の index」というのも間違いではないかな。でも混乱のもとではある (以下)
            *   `[0,1,0,3,12]` で `i=0` のとき、zero_index はそのままの位置に残り、`i=1`のとき、最初の 0 の位置を示している。
            *   `[1,0,0,3,12]` で `i=0` のとき、zero_index は1つ進み、`i=1`のとき、最初の 0 の位置を示している。
            *   ただ、この解釈だと `[1, 2, 3, 0]` みたいなのが与えられたとき、各 iteration で見ると、常に「最初の 0」というのが保証されているわけではないので、やはり混乱のもとかな。
    *   > in-place でなくてよいなら、最初の pass で non zero elements を append して、残り len(nums) に到達するまで zero を追加すればよい。
        *   これよく考えたら in-place で解けるか。最初 non zero を上書きすればいいので (`Solution2`)。
*   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.v62rdhwkdymb
    *   https://github.com/fhiyo/leetcode/pull/54#discussion_r1729801172
        *   > Generator を使って変なコードを書いてみました。
    *   https://github.com/rihib/leetcode/pull/50#discussion_r1888189547
        *   > これ C++ だと zeroIndex == i の場合は未定義動作にあたるかと思いますが、Go では大丈夫でしょうか。
        *   そうなんだ、Python だと問題ないので考えたことがなかった。
    *   https://discord.com/channels/1084280443945353267/1210494002277908491/1211368894669787226
        *   > Erase–remove idiom が頭に思い浮かんでいたら、助けになるかもしれません。
        *   https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom
            *   > These algorithms do not remove elements from the container, but move all elements that do not fit the removal criteria to the front of the range, keeping the relative order of the elements. This is done in a single pass through the data range.
        *   実装例: https://cplusplus.com/reference/algorithm/remove/
    *   https://github.com/Ryotaro25/leetcode_first60/pull/59#discussion_r2007561653
        *   > アンダーフローは、float などで値が0に近くなりすぎて表現できなくなることで、signed integer が負に大きくなることもオーバーフローというようです。なお、unsigned の場合は module 2^n で考えているのでオーバーフローでもないとするのが本来の用語みたいです。

#### Erase–remove idiom

https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom

Erase–remove idiom を Python で書くとこんな感じ？

元のコード

```cpp
template <class ForwardIterator, class T>
  ForwardIterator remove (ForwardIterator first, ForwardIterator last, const T& val)
{
  ForwardIterator result = first;
  while (first!=last) {
    if (!(*first == val)) {
      if (result!=first)
        *result = *first;
      ++result;
    }
    ++first;
  }
  return result;
}
```

C++ の例の `if (result!=first)` のチェックは、同じ index への処理を防ぐものなので、Python では不要な気がする。
> This check avoids copying an element to its own location if no elements have been removed yet.

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        val = 0 # target val to remove
        result = 0 # write index
        # first is read index
        for first in range(len(nums)):
            if nums[first] != val:
                nums[result] = nums[first]
                result += 1
        # If you want to fill the rest by the target val...
        # nums[result:] = [0] * (len(nums) - result)
```

ただし、この例だと、このような出力になる。C++ `remove` はそのように定義されているので問題ないはずだが、LeetCode の問題としては、最後に `nums[result:] = [0] * (len(nums) - result)` のような処理をする必要がある (`Solution3`)

*   Input:    [0,1,0,3,12]
*   Actual:   [1,3,12,3,12]
*   Expected: [1,3,12,0,0]

### step3

*   `non_zero_index` くらいの名前でいいかな？ 途中状態を考えなければ`removed_head` とかでもありなのかな (最終的に、remove された要素 == tail の first index になる)。
