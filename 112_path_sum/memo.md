# 112. Path Sum

https://leetcode.com/problems/path-sum/description/

## Comments

### step1

*   初見から 8:00 程度。
*   DFS か BFS かな。まあどっちでも変わらなさそうだからひとまず DFS で。
*   node の総数の最大値が 5000 なので再帰で書くと recursionlimit あふれるケースはありそう (skewed な tree の場合)。stack で書く
*   コメントで書いているが、`path_sum_so_far` は、ペアになる node の値は含まない sum。
    *   足してから stack に入れた方 (つまりペアの node 自体の値を含む) 方が直感的な気はするが、その処理をスタックに積む段階でやるのはなんか変な気がする (その node 自体についての処理というわけではなくて、次の node の処理を前もってやっていることになるので)
    *   そもそも targetSum から引き算していって、残りの数が 0 だったら return True という手もある

### step2

*   https://github.com/hayashi-ay/leetcode/pull/30/files
    *   DFS、BFS の話、そうか、確かに今回は leaf までいかないといけないので、早く探索を打ち切れる可能性のある DFS の方がよさそう
    *   previous_sum みたいなネーミングはありか
*   https://github.com/nittoco/leetcode/pull/31/files
    *   stack から pop した `path_sum_so_far` に += して変数の意味を変える (今の node を含む sum か含まない sum か) を変えるのが嫌な気がしたので、`path_sum` 変数を別に定義したが、どっちがよいかな。個人的には別定義の方が好みだけど
*   https://github.com/t0hsumi/leetcode/pull/25/files
    *   > 好みですが、私は targetSum は名前的に固定値のままにしたい派です。(https://github.com/t0hsumi/leetcode/pull/25/files#r1981726183)

### step3

*   2:00
*   step2 含めて何度か書いたが特に動きが無さそうなので打ち切り
