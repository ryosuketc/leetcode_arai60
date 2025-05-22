# 1. Two Sum

https://leetcode.com/problems/two-sum/description/

## Comments

### step1

*   定番問題なので3:00 くらいで書いた。
*   for loop の中汚い
*   他の他の解放としては O(N^2) の brute force くらい？空間計算量 O(1) になるやり方あるかな。なさそうだけど。

### step2

*   他の人の解答見る前にちょっときれいにしてみた。
*   `num = nums[i]` を楽しようとして、`for i, num in enumerate(nums[1:]):` と書いてミスった。
    *   `enumerate` はオプションを与えないと 0 からスタートするようだ (TIL)
        *   https://docs.python.org/3/library/functions.html#enumerate
    *   なのでこれをやるなら `for i, num in enumerate(nums[1:], start=1)`
*   今回は解があることが保証されているけど、もしない場合、どう処理するか
    *   step1, 2 では負の値を返すようにしてみた。
    *   空のリストを返す
    *   unreachable 系の exception を上げる
        *   Python だと ValueError かなあ
            *   https://docs.python.org/ja/3/library/exceptions.html#ValueError
            *   https://github.com/takumihara/leetcode/pull/1#discussion_r1806764103
    *   何も書かずに None を返すこともできる
        *   https://github.com/Mahiro-3612/leetcode/pull/1#discussion_r1981011124
    *   終了させる
        *   Python だと `sys.exit('error message')` とか
*   これ、どういうときにどのパターンだと嬉しいんだろう？というのを掘ってみる
    *   https://github.com/Mike0121/LeetCode/pull/50#discussion_r1966726061
    *   コメント集が一番まとまっていた
        *    https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.jdtk9v35bca4

> 放置
Exception を投げる
プログラムを止める
特殊な値を返す
などいくつか対応があり状況次第です。何が好ましいか自問自答する癖をつけて想像しておきましょう。

> ユーザーフェイシングか否か、セキュリティー、パイプラインかリアルタイムか、それ次第で色々ですよね。
https://github.com/fhiyo/leetcode/pull/16#discussion_r1624097270

*   今回のケースでどう処理するべきか一概には難しいけど、通常 index として使わない (というと Python では語弊があるけど)[-1, -1] を返してみたけど、よく考えるとこれは微妙な気がする。
    *   call する側が適切にチェックせずに関数を使うと、nums[-1]に問題なくアクセスできてしまうため。 
    *   もし type hint で指定されている `List[int]` を忠実に守るなら空のリストが一番よさそう。もしくは exception か。

### step3

*   2:16 -> 1:44 -> 1:20