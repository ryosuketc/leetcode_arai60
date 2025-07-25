# 122. Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## Comments

### step1

*   5 mins くらい考えてみたけど前問からどう方針立てればいいかわからなかった。うっすら記憶に谷と山を使ったような気はしたのだけど。

### step2

*   LeetCode ほか複数回答見てみた。
*   `Solution1` の方法は理解さえすれば実装は簡単。前日より上がっているなら前日に買ったことにして売るのを繰り返す。
*   すでに値動きがわかっているので、それを使って game する (Machine Learning for Trading, ML4T の授業で理論上最大利益を求めるので numpy だか pandas 使ってやったことあるの忘れていた)
*   https://github.com/nittoco/leetcode/pull/44/files
    *   参考にして peak / bottom を使う方法を書いてみる (`Solution2`)。
    *   `while i + 1 < len(prices)` と、i + 1 しないといけなかったり、割と書きにくい。関数化して切り出すのは良い。
*   https://github.com/goto-untrapped/Arai60/pull/59#discussion_r1782748689
    *   > 毎日できることは、株を持っているか、お金を持っているかの2択なので、未来が見える人になったとして、どちらがいいかを考えればいいのです。
    *   これ最初どういうことかわからなかったが、`Solution2_3` を見てやりたいことは理解できたので自分で書いてみよう。
    *   `Solution3` 書いたけど変数名長い。
    *   なんかこういう、実際の手触り感ある場面に落として考えるのができてなかった気がする。「未来が見えるとしていつ売買しますか」というような読み替えができるともうちょっとアイデアが出てきたかなという気がする。
*   https://github.com/hayashi-ay/leetcode/pull/56/files
    *   `Solution3` で変数名長くて嫌だったのこれで解決できる (`Solution3_2`)。そう、最初に書いたとき、あ、途中で profit 更新されるから previous じゃないとダメか、と思ったけど、考えたら swap するときの要領で一旦 tmp においておけばよかった。
    *   space O(1) でなくてリストを保持する方法も書いてある (自分の解答では省略)
*   https://github.com/fuga-98/arai60/pull/38/files

### step3

*   profit をちまちま足し上げていく方法が一応一番シンプルに書けるのでこれで。
