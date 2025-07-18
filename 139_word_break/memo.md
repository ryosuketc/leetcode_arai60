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

### step3

*   
