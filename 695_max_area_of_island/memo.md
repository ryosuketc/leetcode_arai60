# 695. Max Area of Island

https://leetcode.com/problems/max-area-of-island/description/

## Comments

### step1

*   とりあえず初見で 10:00 で `SolutionWrongAnswer` を書き上げた。
    *   昨日の問題が SEA / LAND は文字列だったのでそのつもりでやったが、今回は int らしい。
    *   あと SEA も LAND も 0 になっている (typo)
*   明らかに昨日の問題と同じ方針で解けるなあ、と考える。
    *   https://github.com/ryosuketc/leetcode_arai60/pull/17
*   そうするとオプションとしては、DFS、BFS あたり。Union FInd は使えなさそうかな (方法はありそうな気もしたけど、昨日同様DFS での回答が筋が良さそうだなと考えた)。
*   同じく昨日と同様に DFS を再帰で書いてから iterative に直してみようかなと考えた。
    *   さて、引数に何を渡すか10 秒くらい考えた。今回は area (のサイズ) を計算しないといけないので、再帰呼び出しの中でそれまでのサイズを覚えて引き継ぐ必要がある。
    *   引数を 1 個追加すればいいだけ、もしくは好ましくはないように思うけどインスタンス変数に突っ込む方法もあるか？などと考える。`current_area` みたいな引数を追加すればいいだけだろうとは思ったが、ちょっとだけ革新がなかった (20 秒くらい)。
        *   インスタンス変数に突っ込むのは流石に。あくまで関数の中の一時変数みたいなものだし、インスタンスのライフタイムと合わせて存在する意味がわかあない
    *   しかしそもそも iterative に書けば関数内の普通の変数で引き継ぎができるので関数に引数足すなくて良くなる。
        *   昨日の問題では recursion limit の問題で再帰から iterative に直したが、今回は引き継ぎ面で iterative の方がクリーンに書けそうだ。
*   最初の accept 出てから気づいたけど今回は `1 <= m, n <= 50` で再帰の深さは 2500 くらい。ちなみに一般的にデフォルトの recursionlimit は 1000 だと思うが、手元の iPython で試したら 3000 だった。環境によって違うらしい。
    *   https://github.com/python/cpython/blob/9fbd66a93d526c49fac8e1427c25e8f7f4154e29/Include/internal/pycore_ceval.h#L43

### step2

*   https://github.com/colorbox/leetcode/pull/32/files
    *   近い、というか step3 は全く同じ
*   https://github.com/t0hsumi/leetcode/pull/19/files
    *   色々考慮してあって面白い。Union Find、細かく見ていないが、確かに要素数 (rank) 的なものを記録すれば使えるか。
    *   > union-find  は、微妙に常識から外れるかな(多くの人が知っているだろうが知らなくてもドン引きはされない)、くらいの感覚です。DFS による解法のほうは常識でしょう。
        *   https://discord.com/channels/1084280443945353267/1183683738635346001/1197738650998415500
        *   ここの例示はわかりやすかった
*   https://github.com/hayashi-ay/leetcode/pull/34/files
    *   `if (row, col) not in visited and grid[row][col] == LAND:` は内部でチェックしているので不要
*   いくつか解答みてみたが、今回はこのままで十分良さそうだなあという印象。

### step3

*   6:00 -> 5:00 くらい？ (計測漏れ)
*   安定していたので 2 回で終了
