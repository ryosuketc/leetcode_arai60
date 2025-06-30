# 300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/

## Comments

### step1

*   4:00 くらい考えたが、DP の状態遷移をどう定義すればよいのかわからなかった。
*   2 重ループで、「i から始まる subsequence」を調べていく方法はある。

### step2

*   ひとまず LeetCode の、コードは見ずにコンセプトの説明だけ読んで実装してみた (`Solution`)。
    *   たぶん 2 重ループを回す (nums[i] について都度そこまでの dp をすべてチェックしてアップデートする) という発想がなかったと思う。なんとなく O(n) で解けるような先入観があった
    *   `longest_subsequence_lengths[-1]` を return して失敗した。この dp の意味合い、「*その index の数字を使う* subsequence」なので、最後以外が最大になるケースがありうる
*   O(nlogn) の実装があるらしいので、答え読む前に考えるが、これもよくわからない。O(logn) といえば sort かなと考えるが、nums を sort すると subsequence が作れなくなるし、j でループしている方、dp 自体もソートされた順番になっているわけではないので使えない。
    *   答えみたら、そもそも違うアプローチ (`Solution1`) をベースにしていた。
        *   この注釈は面白い。インタビューなら subsequence そのものは間違っている可能性を指摘できないといけない気がする。
        *   > this algorithm does not always generate a valid subsequence of the input, but the length of the subsequence will always equal the length of the longest increasing subsequence. For example, with the input [3, 4, 5, 1], at the end we will have sub = [1, 4, 5], which isn't a subsequence, but the length is still correct. The length remains correct because the length only changes when a new element is larger than any element in the subsequence. In that case, the element is appended to the subsequence instead of replacing an existing element.
    *   これだと、`subsequence` はソートされているので binary search できる (`Solution2`)。
        *   答えを見ずに書いてみたが、ライブラリ使っていいなら簡単。
        *   ライブラリを使わずに実装もしてみたが、詰まってしまった。Binary Search に対する理解がまだ甘い気がする。left を返せばいいというような話 (while が終了するとき、left はそれより左が left より小さいことが保証されているので) (`Solution3`)
            *   https://github.com/ryosuketc/leetcode_arai60/pull/30/files あたりを見て復習した
            *   `right = len(subsequence)` として定義する場合は、right を含まない区間を探索していることになる。ので探索済みの mid 自体にアップデートする: `right = mid` (`Solution4`)
    *   実際のインタビューなら、binary search 部分は関数に切り出すだろう　(`Solution5`)。
*   https://github.com/fuga-98/arai60/pull/31/files
    *   セグメントツリーの解法もあるらしい (深追いしていない): https://github.com/fuga-98/arai60/pull/31/files#r2030043092
        *   TODO: セグメントツリー勉強する
        *   https://discord.com/channels/1084280443945353267/1200089668901937312/1209563502407065602
        *   https://discord.com/channels/1084280443945353267/1210494002277908491/1215698534855090207
        *   https://github.com/TORUS0818/leetcode/pull/33#discussion_r1817859838
            *   > セグメントツリーは、確かに「使えることに気が付きにくいが、計算量を落とせる場合が極めて稀にあり、短時間で書けるくらい単純である」という意味で、プログラミングコンテストに向いているため、競技プログラミング同好会時代にも出てきていました。
        *   https://discord.com/channels/1084280443945353267/1231966485610758196/1300200786050940938
            *   実装についてはこのあたりを参照
    *   https://discord.com/channels/1084280443945353267/1196472827457589338/1343157472742866956
        *   `sys.maxsize` あまりつかったことないなあ、という気持ち
            *   https://docs.python.org/3/library/sys.html#sys.maxsize
    *   `max_lengths` くらいの命名でよかったかな


### step3

*   Binary Search にも課題はあり、セグメントツリーも勉強したいが、DP のセクションなので一旦 DP の問題として練習する

