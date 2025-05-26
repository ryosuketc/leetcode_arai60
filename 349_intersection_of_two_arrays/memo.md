# 349. Intersection of Two Arrays

https://leetcode.com/problems/intersection-of-two-arrays/description/

## Comments

### step1

*   重複排除して intersection を返すらしいので、真っ先に set を使うことを考えた
*   1:00 かからないで accept までいったけど、さすがに簡単すぎるので他の解答など見る前に色々考えてみる
*   ポインタを使うなら、O(N^2) のループで全走査する手段はある。set 分の追加のメモリは食わないけど…
*   両方入れなくても、片方 set にしておいて、もう片方のリストだけを走査することはできる。
    *   nums の配列の長さが unbalance なときは時間計算量と空間計算量のどちらを優先したいかで、どちらをどちらに使うか決める

### step2

*   とりあえず LeetCode を見てみた
    *   なるほど、ソートしてから 2 ポインタを使うやり方もある
*   コメント集を見てみた
    *   https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.o0jquy48e6cy
    *   ポインタ 2 つ: https://discord.com/channels/1084280443945353267/1183683738635346001/1188897668827730010
    *   https://github.com/tarinaihitori/leetcode/pull/13/files#r1827026532
        *   > そこから、merge sort ようなことをする作戦や、片方の値でバイナリサーチをする作戦などがあるでしょう。
    *   https://github.com/katataku/leetcode/pull/12#discussion_r1893968021
        *   > たとえば、追加質問で考えられるのは、「片方がとても大きくて、片方がとても小さいときには、大きい方を set にするのは大変じゃないでしょうか、特に大きいほうが sort 済みのときにはどうしますか。」とかです。
    *   `set_intersection` (C++): https://github.com/Hurukawa2121/leetcode/pull/13#discussion_r1894836342
    *   https://github.com/quinn-sasha/leetcode/pull/13#discussion_r1960884543
        *   > そうですね。この問題は問題文自体では終わっていなくて、解けた後に、いくつか追加の条件が出てきて、その下でのアルゴリズムとそれらの pros and cons が要求されると思います。
*   小さい set を探索して binary search もやってはおきたいけど、時間の都合で今回は merge sort っぽい方を練習してみる。
    *   `nums1 = sorted(nums1)` で引数名を reassign するのはどうかと思うが、そのまま sort すると入力が mutate されるので避けた。本来は `sorted_nums1` とかにするんだけどちょっとさぼった。
    *   共通部分を common という名前に掲げているのよい。linked list の問題でもあったけど、一旦それを掲げてその間は進む、みたいなメンタルモデルになるのでワーキングメモリの消費量が減る。
    *   結果を保持するリスト名は、今回は `result` にした。`intersection` にしたかったけど、set の builtin あたりと被りそうだったので避けた。

#### 追加質問としてありそうなのまとめ

https://github.com/katataku/leetcode/pull/12#discussion_r1893968021

*   「片方がとても大きくて、片方がとても小さいときには、大きい方を set にするのは大変じゃないでしょうか、特に大きいほうが sort 済みのときにはどうしますか。」
   *   小さい方を set にして、その数字を大きい方で binary search
   *   LeetCode だとこういうのがのってるし自分も step1 で考えていたけど、結局どっちも set にしてるからほぼ一緒じゃない？という気はする。まあ小さい方を走査するからいくらか速い気はするけど。

```python
class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
```


*   両方ソートされていてとても大きいときはどうしますか
    *   マージソートの変形。
    *   あれ、結局この書き方 (ポインタ 2 つ) は「マージソートの変形」なんだっけ？マージソートっぽいというのがいまいち理解できていない。
        *   https://discord.com/channels/1084280443945353267/1183683738635346001/1188897668827730010
        *   -> 2 分くらい考えたら理解できた。num1 と nums2 を「それぞれ」半分に分けて merge という話ではなくて、nums1 と nums2 をマージするという話

#### step2 振り返り
*   step1 で他の解法を考えるようにしていたけど、step2 のように深く体系だって理解してはいなかった。
*   step1 で、2 配列の長さが unbalance だったらどうするか、というのもちらっと考えていたけど、それを「追加の条件が出た場合にどういう解法をするか」という一貫した POV で捉えていなかった。別の問題ではそういう視点で色々入出力の条件が変わったときとその解法を体系的に検討していけるように練習したい。
*   TODO: ポインタ 2 つ使うパターンは、全走査しか考えられていなかった。マージソート、大昔に実装したけど、そのうちまたやりたい。

### step3

*   3:00 -> 2:50
*   ちょっと時間なかったのとだいぶ安定していたので 2 回で終了
