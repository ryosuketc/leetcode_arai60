# 2. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/description/

## Comments

### step1

*   とりあえず答え見ずに 13 分くらいで accept まで書ききった
*   ここで 10 がマジックナンバー扱いなのかは微妙な気がする。まあコメント書いたのでいいかなというのと、もしかすると `BASE_NUMBER = 10` みたいな constant を定義するのもいいかも
    *   とはいえどこに定義しようかなという感じではある。まあグローバル汚したくないし class constant かな？
*   直接関係ないけど style guide で、`staticmethod` と `classmethod` をあまり使わないように推奨されている理由がいまだに納得いってない。instance method でよくない？というのはそうかもしれないけど…
    *   https://google.github.io/styleguide/pyguide.html#217-function-and-method-decorators
*   3 つの while loop でほとんど同じことしてるから関数に切り出したい気もするんだけど、なんか複数ポインタを作って、そのポインタを動かしていく、さらに皇族の処理でそのポインタの位置から再開みたいなのがあると、引数で渡してひき回すの、なんか面倒な気がしてしまう…。
    *   後半の 2 つ while を統合するのは関数使わなくても簡単 (`addTwoNumbers2`)。この書き方のほうが、残りの node を処理している感じがあってよいかな。
    *   こっちなら最初のループは node1, node2 を同時に処理、あとのは残ったのを処理、で明確に分かれるし、関数に切り出すにしても微妙に処理が異なるから、関数に出さない理由にもなるので、十分クリーンな気がする。


### step2

*   3:45 くらいで書けた
*   他の人の解答を見る
    *   https://github.com/Mike0121/LeetCode/pull/41/files
    *   https://github.com/nittoco/leetcode/pull/2/files
        *   なるほど、None.next にならないように処理すれば、`while l1 or l2 or carry` でループを一個にまとめることができる。シンプルで DRY だけど、個人的には共通部分をまず処理、残った分を別途処理、という流れのほうがわかりやすい気がする。…とはいえきれいな書き方はこっち (1 ループにまとめる) かな。
*   10 がマジックナンバーか、という上の話、まあ問題文を見れば自明という気もしており、constant として定義するほど意味があるかは微妙な気がしてきた。

### step3

*   8:00 -> 6:30 -> 2:40
*   step3 の初回は step2 の考察を踏まえて 1 ループで書いてみた。こなれていたのでそのまま 2, 3 回目。 
