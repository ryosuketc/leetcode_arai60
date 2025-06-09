# 35. Search Insert Position

https://leetcode.com/problems/search-insert-position/description/

## Comments

### step1

*   5:00 程度で解いた
*   left, index については両端を含む捜査をしているという認識で解いた。そのため while の条件指定については戸惑わなかった。
*   ただ target が見つからない場合 insert position を返すという話で、left / right どちらを返すべきか迷った。結局実際のケースを走らせて確認した。


### step2

*   https://github.com/seal-azarashi/leetcode/pull/38/files#r1834836441
    *   > お題は「すべての値が異なる昇順の配列と target という値が与えられる、target があるならばその場所を、ないならば、それよりも左がすべて target よりも小さくなる場所を返せ」ですかね。
        *   このコメント以降まだ読んでないのだが、「挿入箇所 == それよりも左がすべて target よりも小さくなる場所」とよみかえるとだいぶクリアになったかも。
        *   たとえば nums=[1, 3], target=2 であったとき、最初 left=0, right=1, mid=0 になる。
        *   nums[mid] == 1 (target より小さい) なので、step1 のコードだと else -> left の移動をする。
            *   left が移動するので、処理が終われば left より左はすべてtargetより小さいことが保証されるはず。
        *   次のループではleft=1, right=1, mid=1。nums を見ると 3 でターゲットより大きい。つまり right が移動する。
            *   right が移動するので、処理が終われば right より右はすべてtargetより大きいことが保証されるはず。
        *   ここ、実際の例を通じて left, right の意味するところはある程度理解できたのだが、定義から自明である、と言えるような理解はできるだろうか (上の "left, index については両端を含む捜査をしているという認識で解いた。そのため while の条件指定については戸惑わなかった。" に相当するような感じで)
    *   上記コメントの続きを読んだ
        *   > left を更新するときには、nums[middle] < target を確認してから left = middle + 1 としているのだから、「left は……という条件を満たす」ということを述べて欲しいのです。
        *   -> 上記説明は自分の理解と合致していると思う。nums[middle] < target を確認してから left = mid + 1 としているのだから、left より左の値はすべて target よりも小さいはずである、という話。
    *   > 標準的な bisect_left と異なるのでそこ考えてみましょう。
        *   https://discord.com/channels/1084280443945353267/1225849404037009609/1233211695900528660
        *   https://docs.python.org/3/library/bisect.html
            *   一応 doc 読んだ
        *   https://github.com/python/cpython/blob/cfbdce72083fca791947cbb18114115c90738d99/Lib/bisect.py#L74
*   https://github.com/Fuminiton/LeetCode/pull/41#discussion_r2080995529
    *   > というわけで、書き方を固定してもいいけれども、幅のある表現を読めるようにしてくださいね、ということです。
    *   これ自分が最近ちょっと思っていたことを言語化しているかもしれない。というのも、基本 binary search を書くとき、自分は両端を含むパターンで書くのをできるだけデフォルトにしている気がするので… (なんとなくそれが一番手触りがよい木がしている)
*   https://github.com/hayashi-ay/leetcode/pull/40/files


### step3

*   2:00 前後。特記なし。
