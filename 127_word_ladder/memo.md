# 127. Word Ladder

https://leetcode.com/problems/word-ladder/description/

## Comments

### step1

*   少し考えて、結局 1 文字違いの word 同士を edge で繋いだグラフとして考えれば、グラフの最短経路問題 (BFS) として解けそうだと思う
*   ただ、グラフをどのように represent するかについてしばらく考えて、5 分経過したので解答を見ることにした。
*   初見ではなく、"*" を使って、wildcard 化した文字列を使うような記憶はあったのだが、曖昧だった。
*   LeetCode の回答を眺めた。
    *   一旦それに沿った解答を作ってみた (途中 BFS のところで詰まったので適宜参照した)。
    *   key を求めるところとか、関数化したりしてきれいにはできそうだが、概ね方向性としては、冒頭思った形だと思う (queue 使ってふつうの BFS をする)。
    *   bidiredctional BFS、概念としてはある程度わかるが、コードに落とすの面倒だな…と思ってしっかりコード読むのはやめてしまった…

### step2

*   https://github.com/hayashi-ay/leetcode/pull/42/files
    *   key を求めるの、今回の入力サイズに対してはやりすぎかも。ただ Python だと要件によっては必要かもしれず、過去に解いたことがあるのでバイアスされていたが、そのあたりは (インタビューなら) 確認しながらやるべきなんだろうな (少なくとも最初は愚直な方法が期待されているのではないかと思う)。
        *   https://github.com/hayashi-ay/leetcode/pull/42/files#r1515352706
            *   graph (adj) を作るコードわかりやすい
    *   bidirectional BFS はやりすぎ？
        *   今回、
            *   > Time Complexity: O(M^2  * N), where M is the length of each word and N is the total number of words in the input word list.
        *   あたりを想定すると、上限は M = 10, N = 5000 なので、10^2 * 5000 = 500,000 くらい。一旦定数倍は無視するとして、Python 1 million steps / second くらいだと 0.5 秒？
        *   https://github.com/hayashi-ay/leetcode/pull/42/files#r1515359437
    *   この解答だと BFS を deque を使わずに `get_next_words` で次のすべての word (hit -> `*it`, `h*t`, `hi*` をキーにするようなすべての word) を求めて、それをすべて探索 (BFS の 1 level)。next_words を words に保存しておいて、1 レベル終わったら、words を prev_words に移して、次の level としている。LeetCode の実装とどっちがいいんだろう。
        *   個人的にはそのまま queue を使う LeetCode のやり方の方が馴染みがある気がする？
*   hamming distance、聞いたことはあるけどよく意味がわかってなかった。今回のようなケースで使えるのか…
*   最終、LeetCode の解答の方向で、変数名や関数の切り出しを整理した。

### step3

*   `get_key` にバグがあったせいで 14:00 くらいかかった
    *   正: `return f'{word[:index]}*{word[index + 1:]}'`
    *   誤: `return f'{word[index:]}*{word[index + 1:]}'`
*   14:00 -> 7:00 -> ちょっと時間なかったから 3 回目スキップ

