# 139. Word Break

https://leetcode.com/problems/word-break/

## Comments

### step1

*   ぱっと見、再帰で対象の文字を減らしながら呼んでいって、対象の文字がなくなったら終わりかなと思った。
*   所謂 DP で実装する方法、少し考えたがよくわからなかった。
*   `startswith` の開始位置の使い方をミスっていて詰まった (文字列スライスに対して検索しているにも関わらず開始位置を指定していた)
    *   https://docs.python.org/ja/3.13/library/stdtypes.html#str.startswith
*   一旦素直に書いて、TLE するだろうなと思ったら TLE した (`SolutionTLE`)
*   元々メモ化は必要だと思っていたので 30 秒くらいで `SolutionAC` に変更して AC
*   本当は一つでも True の組み合わせが見つかったら走査を打ち切って return したかったが、どうするのがいいかわからなかった。
    *   現状のコード、見つかっても打ち切らずに全パターンを探索している気がするけど勘違い？
*   TLE について
    *   ただ計算量、ちゃんと見積もれてない。`n = len(s), m = len(wordDict)` のとき
        *   再帰呼び出しの深さ (call stack) は、最大で n になるはず (wordDict に入っているのが長さ 1 の文字ばかりだったとき)
        *   その中で m 回ループしているので、まず O(n * m)。
        *   メモ化していないと呼び出しの木が横に広がって、同じ index での呼び出しもあるはず。O(n^2 * m) とか？あまり自信ない。
        *   メモ化すると O(n * m) 位になるのかな？再帰の計算量まだ苦手かも。
        *   `startwith` しているからここに更に `k = average length of each word in wordDict` が掛け算される感じかな？

### step2

*   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.56p9cz7xyy3h
*   > たとえば、priority queue を用意して、そこに数字 N が入っている場合は「先頭から N 文字目までの部分文字列は、wordDict の結合で表現できる」ということを意味する、とかします。
初期値は [0] (0文字目までは表現できる。)ですね。
    *   DP で解く方法というか、DP の他テーブルをどう定義するのか考えられていなかった。
    *   https://discord.com/channels/1084280443945353267/1196472827457589338/1196541121912909824
*   https://github.com/SuperHotDogCat/coding-interview/pull/23#discussion_r1619222086
    *   step1 で考えていた `startswith` の話

*   https://github.com/katsukii/leetcode/pull/11#discussion_r1929802127
    *   Trie を使うやり方。NeedCode だとこのあたり Trie の話。
        *   https://neetcode.io/problems/implement-prefix-tree
            *   `PrefixTree`: 数年前にははこんなのを書いていたみたい。
            *   今書くなら、`TrieNode` 作って、 `is_word` みたいなメンバを持たせるかな。
        *   https://neetcode.io/problems/search-for-word-ii
        *   https://neetcode.io/problems/min-cost-to-connect-points
        *   今回の問題、Trie 使ってどう解くのかイマイチ理解できてないかも。`startswith` の代わりになるだけ？
            *   TODO: このあたりもう少しちゃんと読む。
            *   https://github.com/katsukii/leetcode/pull/11#discussion_r1929802127
            *   https://leetcode.com/problems/word-break/editorial/
*   https://github.com/TORUS0818/leetcode/pull/41/files
*   https://github.com/hayashi-ay/leetcode/pull/61/files
    *   自分の考えとしては前からやる bottom up DP (`SolutionDpFromFront`) が直感的だと感じていたが、後ろからやる方法もあるか (`SolutionDpFromBack`)。
        *   練習として後ろからも書いてみたが、今 s のどの部分を処理してくか、個人的にはわかりにくく感じた。
    *   TODO: Trie を使う解き方、今回はあまり検討していないので、どこかで復習したい。

### step3

*   TODO: Trie の解き方は後日要確認
*   TODO: DP だと for loop だから計算量が O(n * m * k) なのわかるが (`n = len(s), m = len(wordDict), k = average length of words in wordDict`)、recursion でも同じ計算料になるの、いまいちまだ理解できてないかもしれない。cache してない場合はどうなるんだったか…。
