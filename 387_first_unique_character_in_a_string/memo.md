# 387. First Unique Character in a String

https://leetcode.com/problems/first-unique-character-in-a-string/description/

## Comments

### step1

*   初見から最初の accept まで 3:00
*   ポインタを使って空間計算量 O(1) になるような解答ないかちょっと考えた。
    *   時間計算量 O(N^2) で二重ループでやればいける。
    *   時間 O(N) で空間 O(1) はたぶんないかな…
*   当たり前だけど、今回は配列の最後まで走査するのが必須
*   出現した文字を、dict (count) ではなく set で管理しておくこともできそうだが、1 回だけ出現したやつと 2 回以上出現したやつの区別が面倒 (iteration ごとに set をリセットするとか色々必要)。というか時間計算量 O(N^2) になるか。
*   2 pass から 1 pass にできないかと思ったけど割とややこしそうな気がしている

### step2

*   他の解答見た
    *   LeetCode
    *   https://github.com/hayashi-ay/leetcode/pull/28/files
    *   https://github.com/nittoco/leetcode/pull/20/files
    *   https://github.com/shining-ai/leetcode/pull/15
*   `s[i] in count` は冗長だった (count に入っているのは自明)
*   入る文字列が a-z 限定なら、長さ 26 の配列を使う手もある
    *   step1 では空間計算量 O(N) == len(s) のつもりで を考えていたけど、 s がやたら長い場合でも "s に入っている文字列の種類数" に bound  されることに気づいた。
*   平衡木を使う方法が (C++ だと) あるらしい (深掘りはしてない)
    *   https://github.com/nittoco/leetcode/pull/20/files#r1642843424
*   LinkedHashMap
    *   https://github.com/shining-ai/leetcode/pull/15
    *   Python 的には OrderedDict (3.7 以上なら dict も) と等価という理解
    *   OrderedDict は Linked list 使ってるっぽい
        *   https://github.com/python/cpython/blob/main/Lib/collections/__init__.py
*  そういえば dict は順序が保証されるようになったから、s をループしなくても、count の方をループしてもいい。
    *   > the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.
        *   https://docs.python.org/3/whatsnew/3.7.html
    *   と思って step2 で適当に書いてみたが、よく考えると first_index を保存しておかないといけないので思ったより面倒だった (測ってないが5:00 くらい？) 
    *   多分 dict を {character: first_index} にして、2 回以上出てきたら削除、かつ 2 回以上出てきたことを示す set に入れたほうが見通しがよい
        *   > ああ、2回以上出てきたやつは、普通の set に、1回のやつは、OrderedDict にいれてみたらどうですか?
            *   https://github.com/shining-ai/leetcode/pull/15#issuecomment-1966682629
        *   `Solution2`: そんなに推敲してないけど割に複雑。。
        *   `Solution3`: `next(iter(my_dict))` で dict の最初の要素にアクセスできるみたい。最初 `next(my_dict)` やって失敗したのでとりあえず for ループで書いたんだけど一応それで書き直したのが 3
        *    今回は、dict の最初の要素を返すので使えないが、`popitem` も LIFO を保証するようだ
            *    https://docs.python.org/ja/3/library/stdtypes.html#dict.popitem
        *   最終、dict の order を活かすならこの書き方がよいかな: https://github.com/shining-ai/leetcode/pull/15#issuecomment-1966684185

### step3

*   step2 で色々試したが、結局 step1 て書いたやつが一番わかり易い
*   1:00
*   安定していたので 2, 3 回目は省略
