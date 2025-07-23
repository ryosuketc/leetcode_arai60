# 50. Pow(x, n)

https://leetcode.com/problems/powx-n/

## Comments

### step1

*   特に初見ではなく、ああ、素直に n 乗すると TLE するやつね、という感じ。
    *   -2^31 <= n <= 2^31-1
    *   2^31 = 2,147,483,648 ≈ 2B くらい = 2 * 10^9
    *   2^32 = 4,294,967,296 = 4B = 4 * 10^9くらい
    *   2^64 = 18,446,744,073,709,551,616 ≈ 18 * 10^18
        *   trillion -> quadrillion 以上は面倒で調べるのやめた
    *   実際の数字見ると、C++ だったらぎりぎり計算できるのかな？
*   最初 `Solution1WA` を書いた。
*   しばらく悩んでそもそもアルゴリズムがよくわかってなかったので解答を見て `Solution2AC` を書いた。
    *   n < 0 がありうるのを見逃していした
    *   n % 2 の判定を 1 回しかしていなかったり、result *= result (base *= base ではなく) していたり、そもそもアルゴリズムをちゃんと理解していなかった
    *   LeetCode の書き方は x, n を破壊しているんだけど、変数名も気に食わないし、base と exponent にした。
    *   n == 0 は分けて処理しなくて良い。ループに入らずにresult の初期値のまま返る。
*   解法としては再帰もあるけどループが好き

### step2

*   LeetCode にあるようなこういうの手書きしてみたらよかったかな

```
2^10 = (2 * 2)^5
4^5 = 4 * 4^4
4^5 = 4 * (4 * 4)^2
4 * 16^2 = 4 * (16 * 16)^1
4 * 256^1 = 4 * 256 * (256)^0
```

*   https://github.com/fuga-98/arai60/pull/45/files

*   小数について IEEE 754 などまだ見れていないので後で見る。backlog に追加
    *   https://docs.python.org/ja/3.13/tutorial/floatingpoint.html
    *   https://github.com/ryosuketc/leetcode_arai60/pull/22/files#r2121653075
    *   ちょっと wiki が重かったので応用情報の教科書で勉強した。
    *   浮動小数を`±m * 2^e` で表す
        *   日本語だと、符号、仮数 (m)、基数、指数 (e)
        *   英語だと、sign, significand, base, exponent かな。英語の方がわかりやすい
        *   m は通常何らかの形で正規化する。例えば 0.m で正規化する。
        *   たとえば符号に 1 ビット、指数に 7 ビット、仮数に 24 ビット使うなど
    *   IEEE 754 だと
        *   定義 (32 bits)
            *   sign: 1 bit
            *   exponent: 8 bits (base 2 として、+127 -> bias 127)
            *   significand: 23 bits (significand - 1 の 2 進小数、1.xxx の小数部)
        *   64 bits だと、exponent = 11, significand = 52
        *   significand を 1.xxx で表す。最初の 1. は暗黙に扱えるので 0.m よりも 1 ビット多く扱える。
        *   指数は正負取りうる。負の数を 2 の補数で表すこともできるが、IEEE 754 では +127 して 0 に合わせている。
        *   応用情報の教科書だと、IEEE 754 の仮数 significand - 1 している？
            *   というかそもそも本当に IEEE754 だと -1 しているんだっけ
            *   https://ja.wikipedia.org/wiki/IEEE_754 とちょっと記述違うかも。
            *   大まかな理解はした。応用情報の教科書と wiki の差分はまだそんなに追えてない。
*   ビットを使う解法
    *   https://github.com/olsen-blue/Arai60/pull/45/files
    *   https://github.com/hayashi-ay/leetcode/pull/41/files#r1515417145
    *   e.g. 3^14 = 3^(2^3) * 3^(2^2) * 3^(2^1)
    *   正直なところまだ腹落ちしきっていない (powered / cumulated が自然言語で何を示すのか言語化できていない) が、時間的都合で一旦 backlog 行き…。あとで悖る。ビット演算の復習はすべきかも。
*   ビットの方がコンピュータっぽいが、数学的な (人間がやる) 計算を模倣した step1 のやり方ができるのが先かなということで step1 の方で練習。

### step3

*   2:30
*   書いていて思ったが step2 のビットで腹落ちしていないのって、変数名の定義の他には、多分こちらの (step1 ベースの) 解答でも当てはまっていて、result を、exponent % 2 == 1 のときにしかアップデートしていないからな気がする？
    *   result はループの中で (exponent が減るときは) 毎回アップデートされてほしいという気持ちがあるかも。なんか base の方にためておいて、exponent % 2 == 1 のときに一気にアップデートするというのに納得がいってない気がする。。
