# 33. Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/

## Comments

### step1

*   最初 `Solution1` を書いて WA　(8:00 くらい)
    *   前問 (https://github.com/ryosuketc/leetcode_arai60/pull/31) の考えを踏襲して、まず崖を登る、降りるで大きく場合分け。nums[middle] と target を比較。
*   少し考えて、nums[middle] と target を比較だけでは不十分なことに気づいた。mid が崖を登っている場合、nums[mid] < target なら答えは右側 (さらに登った先) にあることは確定する。ただ target < nums[mid] の場合は、target が登っている途中 (左) にあるのか、降りた後 (右) にあるのかが確定していない。そのため target を nums[-1] と比較して、どちらにあるか調べる必要がある。
*   ここまで考えて実装。確信が持てたので submit したら、21:00 くらいで accepted
*   時間はかかったが一旦答えを見ずに解き切れたのはよかったかも。前問を解く前だと、場合分けや境界の条件に苦労して結局解ききれなかったように思う。
*   上記の考えに基づくと、そんなに複雑な分岐はしていない (コードに落とすのは簡単) が、見た目的には if / else がたくさんぶら下がっていて少し気持ち悪い感じはする？もっとシンプルにする方法あるかな？

### step2

*   https://github.com/hayashi-ay/leetcode/pull/49/files
    *   ここだと x 側が「昇順に並んでいる」という表現をしている。私の表現だと、崖を登っている場合はその点より左が sorted、降りている場合は右が sorted。sorted であれば `if nums[left] <= target <= nums[mid]:` などのように target の範囲を限定して、あとは else というまとめ方ができる。
    *   pivot_index: なるほど、min つまり崖の境をまず求めるという方法もある
*   bisect_left を使った解法
    *   元ネタ: https://github.com/Yoshiki-Iwasa/Arai60/pull/36/files#r1712955053
    *   https://github.com/fuga-98/arai60/pull/43/files
    *   https://github.com/olsen-blue/Arai60/pull/43/files
    *   面白いがこれは思いつかないかな…
    *   https://docs.python.org/3/library/bisect.html
    *   `(num <= nums[-1], target <= num)`
        *   結局これを key にソートしようとしているイメージ？
        *   まず nums[-1] との大小で絶対的な序列が決まる。num <= nums[-1] であれば、より小さい方の山にあるはずなので、T。崖を登っているのが F (0), 降りた後なのが T(1)。今回は F の方が序列が高い (昇順で先にくる)。
        *   次に target と比較して、target 未満が F、target 以上が T。
        *   これを使うと
            *   崖を登っている (F) and target 未満 (F)
            *   崖を登っている (F) and target 以上 (T)
            *   崖を越えたあと (T) and target 未満 (F)
            *   崖を越えたあと (T) and target 以上 (T)
        *   という順番に並ぶ。

```python
def priority(num, nums, target):
    return (num <= nums[-1], target <= num, num)

def get_keys(nums, target):
    keys = []
    for num in nums:
        keys.append(priority(num, nums, target))
    print(f'nums={nums}')
    print(f'target={target}')
    print(f'keys={keys}')
    return keys

nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
keys = get_keys(nums, target)

nums=[4, 5, 6, 7, 0, 1, 2]
target=1
keys=[(False, True, 4), (False, True, 5), (False, True, 6), (False, True, 7), (True, False, 0), (True, True, 1), (True, True, 2)]

nums = [4, 5, 6, 7, 0, 1, 2]
target = 5
keys = get_keys(nums, target)

nums=[4, 5, 6, 7, 0, 1, 2]
target=5
keys=[(False, False, 4), (False, True, 5), (False, True, 6), (False, True, 7), (True, False, 0), (True, False, 1), (True, False, 2)]

```

ここまで試して、bisect の話わからんなあ、と思っていたが、index を見つけるところ

```python
index = bisect_left(nums, priority(target), key=priority)
```

なので、target 自体を探しているわけではなく (target を探していると思っていた)、priority の返り値 = (bool, bool) を探している。ので、その返り値が出てくる一番左を返している。priority(target) は、定義から FT か TT (後ろが target 以上で True なので) のどちらか。

うーん、やっていることはわかったのだが、正直なぜこれ (`priority`) で target の位置になるのかイマイチ納得はできていない。。

*   `Solution1`: bisect のやり方で一応書いたのを残しておく。まだ 100% 理解できてない。
*   `Solution2`: インタビューであればこっちのやり方が想定される気がする。落ち着いて場合分けするのがポイントか。
*   `Solution3_WA`: 半開区間 (right は含まない) で書こうとして失敗。
    *   https://github.com/hayashi-ay/leetcode/pull/49/files
    *   `Solution3_AC`: right は含まないんだから、right = middle だ (middle を探索済みにする)。あと nums[right] も nums[right - 1]
*   慣れの問題かもしれないが、閉区間の方が書きやすい気がした

### step3

*   特記なし。閉区間のパターンで練習。
