# 20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/description/

## Comments

### step1

*   5:00 くらいで何も水に書いてみた。典型問題すぎて暗記しているみたいなところはあるかも。
*   とはいえ、実際あまりきれいに書けた気がしない
    *   `char` は別によくないかも。`brackt` とかかな。
    *   変数名、`stack` はただの内部実装を表す名前だからもっと処理の中での意味的なものにしたいかも。`appeared_brackets_stack` とか？ `unmatched_brackets` とかでもいいかも。
    *   `brackes_map` は、後で closing -> opeing の map を使うからこういう構造にしたけど、これももうちょっと説明的な名前でもいいのかも。`closing_to_opening_brackets` とか？
    *   `stack.pop() != brackets_map[char]:` は、一旦変数にアサインして名前をつけてもいいかも。
        *   `actual_pair = stack.pop()`
        *   `ecpected_pair brackets_map[char]`
        *   とか？ actual, expected っていうとテストっぽいけど。
*   stack 以外使うやり方思いつくかなーとか 2 分くらい考えたけど、まあ stack 使っているということはほぼ自明に再帰でかけるなーくらい。今回だとどっちでもいい気がする。

### step2

*   命名はともかく、全体の処理の流れとしてはより改善するあんがぱっと思いつかなかったので他の人の答え見に行く。
*   https://github.com/Fuminiton/LeetCode/pull/6/files
*   https://github.com/Mike0121/LeetCode/pull/2/files
*   https://github.com/TORUS0818/leetcode/pull/8/files
*   変数名は step1 で考察した感じをベースに書きながら考えるといいかも。方向は良さげ。
*   `not stack` かどうかの判定は独立の if clause にしたほうがわかりやすいかな
*   この時点でざざっと書いてみた (`step2-1`)が、open bracket のとき (`else`) の処理が、短いのにだいぶあとに来ていて読みにくい
*   `step2-2` にリライト。だいぶ読みやすい気がする。まあ actual... / expected... の変数にアサインするのは過剰かもしれない。

### step3

*   2:20 -> 1:50 -> 2:10
