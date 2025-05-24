# 49. Group Anagrams

https://leetcode.com/problems/group-anagrams/description/

## Comments

### step1

*   初見からゆっくり解放考えて実装完了までで 6:30 くらい。
*   sort したやつを key にして dict に入れる以外の解法が思いつかなかった。

### step2

*   使われるのがa-z の 26 文字限定なら、count を保持した長さ 26 の array を key に使える。
*   big O notation 的にはこっちのほうが logN 倍速いけど、実測どれくらい違うんだろう？26 文字以外に対応したくなったとき大変だし、いろいろな文字列に対応できる sort の方が usability / maintainability 的に優れているように感じる。
*   defaultdict
    *   https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    *   https://docs.python.org/3/library/collections.html#collections.defaultdict
*   https://github.com/nittoco/leetcode/pull/13/files
    *   上記あたりを参照すると`__missing__` が実装されているようだ
*   `__*__` のメソッドって一般的になんて呼ぶんだっけ、magic method でいいんだっけと思って調べたけど一応正式には special method というらしい。
    *   https://github.com/nittoco/leetcode/pull/13/files
    *   > An informal synonym for special method.
*   このあたり参照して自分で書いてみた。
    *   https://discord.com/channels/1084280443945353267/1225849404037009609/1228028878589657150
    *   これ、dict を継承して magic method をオーバーライドして実装したけど、実際の面接だと dict をインスタンス変数に持った形で実装するかも (どの magic method をオーバーライドすべきか悩むし)
        *   `MyDefaultDict2` を実装してみたけど、やはりこっちのほうがしっくり来る。まあ `values()` みたいな dict にデフォルトであるメソッドをそのまま呼べないのがアレだけど。。

### step3

*   2:30 -> 1:40 -> 1:20
*   今回は defaultdict を使った
*   `for s in strs` の変数名が s でよいかはいまだにちょっと迷う
    *   str は builtin だし、かといって今回は (意味のある) `word` 限定というわけでもないし。
