# 8. String to Integer (atoi)

https://leetcode.com/problems/string-to-integer-atoi/

## Comments

### step1

*   これはアルゴリズムというか、単に要件を順番に実装していくだけ。
*   `Solution1`: 2 回ほど WA 出しつつ、21:00 くらいかかって AC。ちょっと遅いなあ。
    *   l25 の `result //= 10` を忘れていた。直前のループで `result *= 10` が、最後の桁の数字に対してもかかるため。これ汚いので推敲して消したい。
    *   `+` のときに `i` を進めるのを忘れていた。
    *   一番最初 for loop で書こうかと思ったけど、leading whilespaces / zeros の処理などで却ってわかりにくくなる印象だったのでやめた。
    *   MIN_INT, MAX_INT の処理については、本来は超えたら、あるいは次で超えることがわかったら return してよいのだが、Python なのでそこまで気にせず最後まで処理してから最後に判定することにした。「次を処理することによって超えるか」という判定は 32 bit int しか使えない環境だと割に面倒かもしれない。64 bit を使えるなら超えてから超えたかどうか判定すればよいのでシンプル。
*   leading whitespaces / zeros を preprocess した文字列を作って、その文字列に対して for loop とかがわかりやすそう。
    *   -> `Solution2` 書いてみた。思ったよりはきれいじゃない。
        *   `preprocess` の返り値を保存する変数名、もうちょっとまともなのになってほしい。`preprocessed_s_start_index` とかかな。長いけど。もしくは文字列のコピー取ることになるが、`preprocess` で `s[i:]` を返す手もある。
*   https://docs.python.org/3/library/stdtypes.html#str.lstrip
    *   `Solution3`: built-in 使って、文字列コピーの計算量をあまり気にしないパターン。
*   そういえば `Solution1` の冒頭に

### step2

*   https://github.com/shining-ai/leetcode/pull/59/files
    *   https://docs.python.org/ja/3/reference/expressions.html#binary-arithmetic-operations
        *   > The modulo operator always yields a result with the same sign as its second operand
        *   おなじみ負の数を `%` したときの挙動の話。
    *   overflow をきっちり処理するなら `is_overflow` 的な関数に切り出すほうが良さそう。
*   https://github.com/Yoshiki-Iwasa/Arai60/pull/64#discussion_r1747497750
    *   > 一応、MIN = - MAX - 1 は念頭にありますね。
    *   そこまで意識せずに書いてしまったかも
*   https://github.com/katsukii/leetcode/pull/9/files#r1919816731
    *   > Java には、multiplyExact、addExact というのがありますね。
    *   overflow したときに例外投げるというやつらしい。Python の例外はまあそんなに重くないだろうし、そういう関数の実装もありかと思った。
    *   C++ だとこういうのあるみたい: https://github.com/philip82148/leetcode-swejp/pull/6#discussion_r1853735872
*   > 「次を処理することによって超えるか」という判定
    *   step1 のこのあたりは皆さんちゃんと処理している。問題の期待はそっちにもあるのかな。

```python
-1 % 10 # 9
int(math.fmod(-1, 10)) # -1
-1 // 10 # -1
int(-1 / 10) # 0 - rounded to zero
```

*   https://github.com/hayashi-ay/leetcode/pull/69/files
    *   私は組み込みで `int(s[i])` としていたが、なるほど、`int` を使わないなら `ord` で書けるか。
*   https://github.com/olsen-blue/Arai60/pull/60/files
*   `step2.Solution`
    *   上記参考にして書いた。
    *   `is_over_limit = result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > MAX_INT % 10)`
        *   `(result == MAX_INT // 10 and digit > MAX_INT % 10)`
            *   `result == 214748364` のとき、次の計算では `2147483640 + digit` になる。
            *   `MAX_INT == 2147483647`, `MIN_INT == -2147483648`
            *   なので、digit が `MAX_INT % 10 == 7` より大きい、つまり 8, 9, 10 の場合に overflow / underflow が発生する可能性がある。厳密には正の数の場合、8, 9, 10 のいずれでも overflow、負の数の場合、8 であれば溢れているわけではないが結局返す値は `MIN_INT` になる。
                *   https://github.com/Ryotaro25/leetcode_first60/pull/59#discussion_r2007561653
                    *   underflow / overflow という言葉の使い方が正しくない気がするので調べた
                    *   > アンダーフローは、float などで値が0に近くなりすぎて表現できなくなることで、signed integer が負に大きくなることもオーバーフローというようです。なお、unsigned の場合は module 2^n で考えているのでオーバーフローでもないとするのが本来の用語みたいです。
                    *   つまり今回だと正でも負でも overflow か。
    *   関数切り出しも考えたが、今回は関数全体として文字列を前から走査して処理するので、あえて個別の関数には切り出さずに sequential に書いたほうが書きやすく読みやすいと感じた。適度にコメントで処理の塊を示すくらいで良さそう。


### step3

*   7:00 くらいで書けた。
*   `MAX_INT` とか `MIN_INT` が一般的な形容詞の順序なのでそっちを使っていたが、`INT_MAX`, `INT_MIN` としている人が多かったので一応調べる
    *   https://cpprefjp.github.io/reference/climits/int_max.html
    *   なるほど、C++ だと `INT_*` なのか。一応そっちに統一。
*   `i` よりも `index` の方がよいというコメントが来そうな気もするが、今回は単純に文字列を最初から順番に走査している単純な用途なので短くて良い気がする。他に index が出るわけでもないし。
*   ちなみに演算子の優先順位は `not` > `and` > `or` なので
    *   `result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10)`
    *   の括弧はなくても全く同じ意味になる。ただ場合分けしているのをわかりやすくするためだけの括弧。
    *   https://docs.python.org/ja/3.13/reference/expressions.html#operator-precedence
