# 103. Binary Tree Zigzag Level Order Traversal

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

## Comments

### step1

*   level order traversal とほとんど一緒か、と思って解く
    *   https://github.com/ryosuketc/leetcode_arai60/pull/26
*   8:30 くらいで書き上げたのだが、最後の get_direction を使った下り、これだと動かないことに気づく
    *   これだと level = 1 のときに、R to L で追加して、R から順番に処理、次の level は L to R だが、level = 1 の一番右の左の子どもから追加するだけなので、全体として L to R にならない。
    *   このままでも最悪最後に奇数番だけ reverse する手はあるが。
*   前の問題の step1 のように for を使ってレベルごとに iterate するほうがよいかな？
    *   7:00 くらいで `Solution2` -> Accepted
    *   最初間違えて `nodes_in_this_level` ではなく `current_level` を reverse していた。

### step2

*   

### step3

*   
