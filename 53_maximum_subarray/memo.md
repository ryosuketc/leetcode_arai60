# 53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray/

## Comments

### step1

*   DP の問題だし、ということで遷移を考えてみる。
*   max_sums のような dp 配列を管理、nums を順番に見ていく？ i - 1 -> i に遷移するとき
    *   1. nums[i - 1] に nums[i] をつける
    *   2. nums[i - 1] に nums[i] をつけない
    *   3. nums[i] だけ使う
*   の三択で max を取る？ -> サンプル走らせてみて違う、となる。
*   よくわからないのでとりあえず brute force。何もしなければ O(n^3) だが、建材の subarray を変数として管理して足していけば O(n^2) までは簡単。一応書いてみたが TLE `SolutionTLE`
    *   特に最適化にはならないが、累積和として解くこともできる

### step2

*   7:00 くらい考えてLeetCode の解法見る。
*   よく考えたら上記の 3 択は違う。subarray だから連続している必要があり、2 だと一旦配列を切ることになるので、3 のシナリオになる。なので正しい選択肢は 1 or 3。つまりそこまでのsubarrayに nums[i] を追加するか、subarray をリスタートして nums[i] だけ使うか。
    *   LeetCode の解法 = `Solution1` はまさにこの形。subarray が現在の subarray で、その二択を管理している。
    *   dp 配列を管理する方法でも解いてみる
        *   さっと書けた気がしたが WA (`Solution2WA`)
        *   正しくは `Solution2` -> `return max(max_sums)`
        *   `[-2,1,-3,4,-1,2,1,-5,4]`
            *   `i=6` で max_sums[6] = 6 となり最大、負数があることによりそれ以降はより小さくなる。
        *   `Solution2` の space optimization をしたのが `Solution1`
*   遷移について惜しいところまで考えられていたので、`Solution2` くらいは自力で書けたかも。
*   全然思いついていなかったが LeetCode に divide and concur の話があったので一応書く
    *   この問題だったか忘れたが、middle element を含むかどうか、みたいなので最大値を取る問題どこかでやった気がする。
    *   解答を参考にしつつ、`Solution3TLE` をとりあえず書いてみた。TLE する理由 (他は正解) がよくわからなかったが、解答と見比べたら、for loop のときに left / right の boundary を考慮せずに全部探索していた (`Solution3`  で修正)
    *   別に `Solution3` でもよかったのだが、2 個めのループで `for i in range(mid + 1, right + 1):` と、`right + 1` しているのがなんだが気持ち悪いので、right は含まない方法で書き直した (`Solution4`)。数回 WA を挟んだけど、単純な見落としで、半開区間で書くか閉区間で書くかみたいな話は (少なくともこの問題では) うまくできたように感じる。
*   https://github.com/hayashi-ay/leetcode/pull/36/files
*   https://github.com/fuga-98/arai60/pull/32/files
    *   上記書く中でこのあたりの解答を眺めた
    *   私は max を取る方法ばかり考えていたけど、それまでの subarray が負であるかを考える方法もあるか。
    *   https://discord.com/channels/1084280443945353267/1206101582861697046/1207405733667410051
        *   Kadane の名前がつく程度のアルゴリズムであるらしい。常識外。ただいきなりは思いつかないけど、step1 に書いたような DP 配列を保持する方法から始めれば割と自然に出てくるような気もする？？
            *   その発想に至るまでのプロセス: https://discord.com/channels/1084280443945353267/1206101582861697046/1208414507735453747
                *   > 累積和を利用して、差を取って、和を求めているんだったら、最大値を出すときに、その時点での最小値を求めればいいはずですね。
                *   「その時点での最小値を求めればいいはずですね」のところ実はわかってない
                *   と思って https://github.com/sakupan102/arai60-practice/pull/33/files#r1611415355 を眺めたらわかった。差を求めているんだから、トータルの数を最大化するには、引く数が最小であればいいよね、という話か。
            *   標高の話とか: https://github.com/olsen-blue/Arai60/pull/32#discussion_r1962010150
    *   https://github.com/Fuminiton/LeetCode/pull/32#discussion_r2050179980
        *   > あー、そもそもの話として、maximum_subarray に負の小さい値を入れるというのが「番兵」であるという認識はありますか。
        *   番兵と言うと、Linked List のイメージがあったが、なるほどこういうのも確かに番兵か。
    *   https://github.com/Fuminiton/LeetCode/pull/32#discussion_r2050216094
        *   分割統治に関する感想。今回の問題でわざわざ出す？DP で解けるのに面倒では？という感想だったが、その理由の言語化はこれかな (mid をまたぐときの処理が面倒)。まあ発想の幅という意味では練習としてはいいか、くらい。
        *   > 左右の分割 + O(n) は、たとえば、最大の内点を含まない長方形などでたまに出てくる気がします。今回はどんぴしゃという感じはしないですね。

### step3

*   何回か書いたけど、結局 `Solution1` のように i=1 から始めるのがちょっと気持ち悪くて、`Solution2` に落ち着いた。
*   `subarray_sum` をリセットしながら進むので、sliding window っぽい形でもある
