# 103. Binary Tree Zigzag Level Order Traversal

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

## Comments

### step1

*   level order traversal とほとんど一緒か、と思って解く
    *   https://github.com/ryosuketc/leetcode_arai60/pull/26
*   8:30 くらいで書き上げた (`Solution1`)のだが、最後の get_direction を使った下り、これだと動かないことに気づく
    *   これだと level = 1 のときに、R to L で追加して、R から順番に処理、次の level は L to R だが、level = 1 の一番右の左の子どもから追加するだけなので、全体として L to R にならない。
    *   このままでも最悪最後に奇数番だけ reverse する手はあるが。
*   前の問題の step1 のように for を使ってレベルごとに iterate するほうがよいかな？
    *   7:00 くらいで `Solution2` -> Accepted
    *   最初間違えて `nodes_in_this_level` ではなく `current_level` を reverse していた。

### step2

*   https://github.com/hayashi-ay/leetcode/pull/35/files
    *   reverse しないなら deque で、偶数ならappend、奇数ならappendleftをするといった実装もある
*   https://github.com/t0hsumi/leetcode/pull/27/files
    *   nonlocal の話が勉強になった (https://github.com/t0hsumi/leetcode/pull/27/files#r1984365150)
*   `reverse`, `reversed` の doc を眺めた
    *   https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
    *   https://docs.python.org/3/library/functions.html#reversed
*   reverse するほうが可読性が高いかなという気もした (かつ level ごとに O(N) 必要なだけで、どちらにしても O(N) で node をなめているので、そこまで大きなインパクトはないように思う)
*   が、たまには deque を使ってみようという気になったので、深いこだわりはないが、deque を使って練習してみる
*   https://docs.python.org/3/library/functions.html#reversed
    *   ついでに眺める。
    *   > and is short for “double-ended queue”
        *   知らんかった
    *   > If `maxlen` is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end.
        *    これも発見。なるほど、自動で window みたいな使い方ができるのか…
    *   今回のように loop ごとに deque を作り直す場合、再定義するのと、既存のを `clear` するのとどっちがよいのだろう？
    *   `rotate` しらんかった
*   9:50 くらいでゆっくり変数名とか考えながら書いてみた (`Solution1`)
*   二重ループを関数に切り出す方法もあるかと思って `Solution2` を書いてみた。ちなみに今回は nodes と level を引数に渡したが、読んでいるだけなので別に引数で渡さなくても inner function (`get_zigzag_order_and_next_level`) から外のスコープにアクセスはできる。個人的には inner function で外側の何を使っているかわかりやすいので引数として渡したいのだが、となると inner function であるメリットはさほどないかなと思う。隠蔽できるとか、外の関数と密結合であることはわかりやすくなるが、単回の関数としては切り出して使ったりメンテしにくくなる気がする。もちろん引数がもっと多ければそれを引き回すのは…という気もするが。

### step3

*   6:30 -> 4:30 -> 5:00
*   書いているうち `nodes_next_level` ではなくてより短い `next_nodes` で良い気がしてきた (そもそもコンセプト的に `nodes` が current level の node を保持しているので)
*   慣れると空行が減るというのを色々な人がコメントしていて、なぜそうなるのかよくわからなかったが、今回の問題なんとくわかった気がする。結局脳内でちゃんと処理できていると、フォーマットとして空行を入れなくても脳内で意味ごとのブロックに分解できる (コードを読み書きするときの解像度が上がる？) ような気がする。
