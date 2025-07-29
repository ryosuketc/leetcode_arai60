# 31. Next Permutation

https://leetcode.com/problems/next-permutation/

## Comments

### step1

*   5:00 くらい考えたけど方針が立たなかった。次の permutation、というのがどういうものかうまく整理できなかった。
*   まず LeetCode の解答見た。アルゴリズムとしてはなんとなく理解できる。
    *   decreasing order が最後の perm。
    *   ということは、まず decreasing order になる index (厳密には、それより左が全て decreasing order になる index == `left`) を探す。
    *   decreasing order が最後の perm なので、decreasing order の部分だけをいじっても next perm は作れない。
    *   decreasing order の中から、`left` (`4`) より大きい (ものの中で最小) == `right` (`5`) を探す
    *   `left`, `right` を swap する
    *   すると、left までは next perm になる。left + 1 以降は、現状 decreasing order だが、最初の perm にする必要があるので、reverse する。
    *   e.g. `[1, 5, 8, 4, 7, 6, 5, 3, 1]`
        *   `nums[left] == 4, nums[right] == 5`
*   他の解答コードを見る前に、自力で書けるか試してみたが、エッジケース (全て descending とか、全て ascending とか) を逐次考えていくと段々わからなくなってしまった。

### step2

*   https://github.com/hayashi-ay/leetcode/pull/67/files を参考に書いてみる (`Solution1`)
    *   なぜ `rfind` という命名にしているのか最初わからなかったが (`rfind` をあまり使ったことがないので)、なるほど、最後から検索するという意味で使っている。見つからなかったときに -1 を返すのもこれに準拠している。
        *   https://docs.python.org/3/library/stdtypes.html#str.rfind
    *   この手順がうまく整理されている
        *   > 1. 右からみて昇順でない数を探す。（降順になっている部分は並べ替えが済んでいる）
        *   > 2. 1で見つけた位置からその数より大きい最小の数値を探す（1で見つけた数値を次に大きい数値で置き換える）
        *   > 3. 1て見つけた位置の右側を反転させる（2の段階で降順になっているので昇順になおす）
*   https://github.com/olsen-blue/Arai60/pull/59/files
    *   > 棒グラフのイメージがしっくりきた。高い棒グラフを前方にある低い棒グラフを入れ替えると辞書順で後にする、という処理になる。
    *   > 後ろから逆向きに arr を見たときに上り坂の範囲は、そもそも辞書順で後にする処理ができないので、初めて下り坂になる部分を見つける。
    *   > 下り坂の部分により大きな値を入れると、辞書順で後にできる。その値は可能な限り小さい方がよく、末尾～現時点までで見てきた数の中から交換相手を選んで交換する。
        *   > (追記)交換相手は、末尾から見ていって最初にnums[left]を超える値でOK
    *   > 交換後、すでに辞書順で後になってるが、「辞書順で直後」の状態を目指すために、極限まで貪欲に近づける形で、left + 1 ~ 末尾を昇順にソートして仕上げをする。
    *   https://github.com/olsen-blue/Arai60/pull/59/files#r2033591275
        *   > 平均計算量は、可能な全入力に対しての平均です。たとえば、クイックソートならば、全順列を入れてみて平均を取ります。
        *   > 償却計算量は、ある最悪な入力の列に対しての振る舞いのことです。
        *   > たとえば、list に append していくと、たまに、メモリーのリアロケーションで配列長かかりますが、大きさが倍々に増えていく場合(倍でなくても等比級数的ならばよい)は、reallocation のコストは定数で平均すると抑えられます。
        *   > 何も言わずに計算量と書くと、最悪計算量のことを指すことが多いですね。これは最悪な入力に対しての計算の増え方がある関数で抑えられるということです。
        *   この解法 (以下引用) `nums[pivot] >= nums[swap]` つまり descending order である限りはスキップ。ascending になる場所が見つかったらそれ以降を reverse して終了。ちょっとわかりにくい気はするので練習はしないが参考として引用しておく。

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for pivot in range(len(nums) - 2, -1, -1):
            for swap in range(len(nums) - 1, pivot, -1):
                if nums[pivot] >= nums[swap]:
                    continue
                nums[pivot], nums[swap] = nums[swap], nums[pivot]
                nums[pivot + 1:] = reversed(nums[pivot + 1:])
                return
        nums.reverse() 
```

*   特定範囲を reverse する built-in あるのかと思ったが、 `reverse`, `reversed` とも index 的な引数は取らないらしい　(スライスを渡して置換は可能だが)。
    *   https://docs.python.org/3/library/stdtypes.html
*   上記諸々踏まえて `Solution2` 書いてみた。
    *   特に `rfind_first_not_descending` の返り値はちょっとトリッキーな挙動が多いので production なら function docstring をちゃんと書くのだが、inner function なのでふつうのコメント中心にしておいた。
    *   `reverse_in_range`、`*_range` という命名の割に `end` inclusive なのは少し気になるが。
        *   `reverse_in_range2` のように `end` を上書きしてしまうのが一番早いが、引数の意味合いを関数で返るのはよくないかもしれない。 immutable なので引数自体が変更されるわけではないが。

### step3

*   7:30 くらい
*   こういう、各処理が複雑なやつは関数だけ定義してメインの処理をまず書くことにフォーカスするとよさそう。中身は後で。
    *   ただこのアプローチ、すでに何回か書いてアルゴリズムとコードの書き方が頭に入っているからすんなりできている部分はある。実際は関数の命名や、どこを関数に切り出すか、もっと試行錯誤が必要になるだろう。

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j) -> None:
            pass

        def rfind_first_not_descending() -> int:
            pass
        
        def rfind_first_greater_than(target: int) -> int:
            pass
        
        def reverse_in_range(start: int, end : int = len(nums) - 1) -> None:
            pass
        
        pivot_index = rfind_first_not_descending()
        if pivot_index == -1:
            nums.reverse()
            return
        swap_index = rfind_first_greater_than()
        swap(pivot_index, swap_index)
        reverse_in_range(pivot_index + 1)

```
