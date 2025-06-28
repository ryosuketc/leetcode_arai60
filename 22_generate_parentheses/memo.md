# 22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/

## Comments

### step1

*   たとえば `n=3` だったら、opening parentheses は、3 つまで連続で追加できる。つまり
    *  `(`, `((`, `(((`
*   の 3 パターンがあり、それぞれにどのタイミングで close していくか、という選択肢がある。
*   `(` で始まったら
    *   すぐ close するしかない -> `()`。となると後は `n=2` について再帰的に解く
        `n=2` だと、`(())` または `()()` なので、最終的に`()(())`,`()()()` が返る (2 通り)。
*   `((`
    *   1 つ close -> `(()`
        *   ここから再度 open もできる (`(()(...`) し、close してしまうこともできる (`(())`) (2 通り)
*   `(((`
    *   すべて close するしかない: `((()))` (1 通り)
*   結局今開いているやつと閉じているやつの数を管理しながら構築する必要はありそうだとぼんやり思ったが、うまくコードに落とせなかった。
*   手作業なら、`(` と `)` のカードを 3 つずつ持っていて、それを順番に並べていくイメージかな。上のように、まず最初に `(` を何個並べるかというので分けて試していくようには思う。

### step2

*   答え見れば何をやっているかはわかる。step1 で書いた手作業の感覚に backtrack が一番近い。
*   https://github.com/hayashi-ay/leetcode/pull/70/files#r1548084966
    *   全通り出力して有効な括弧が判定するというのはそういえば考えていなかった。確かに n 小さければそれでもいいのか。
    *   以下のように left (opening) だけ管理しても解ける

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_valid_parentheses = []
        partial_parenthesis = []

        def make_parenthesis(index, num_left_brackets):
            if index == n * 2:
                if num_left_brackets == 0:
                    all_valid_parentheses.append("".join(partial_parenthesis))
                return
            
            if num_left_brackets > 0:
                partial_parenthesis.append(')')
                make_parenthesis(index + 1, num_left_brackets - 1)
                partial_parenthesis.pop()
            
            if num_left_brackets < n:
                partial_parenthesis.append('(')
                make_parenthesis(index + 1, num_left_brackets + 1)
                partial_parenthesis.pop()
        
        make_parenthesis(0, 0)
        return all_valid_parentheses
```

*   https://github.com/nittoco/leetcode/pull/43/files
    *   `yield`, `yield from` をうまく使っている。Generator は使いこなしたいがまだぱっと選択肢に上がってこない
    *   `generator_cache` というアノテーションを定義して使っていたりする。このあたりは正直あまり理解が追いついてない。
*   https://github.com/fuga-98/arai60/pull/52/files

### step3

*   TODO: もうちょっと他の人の回答を読み込みたいが、時間切れ。。一旦 review 出します。
*   解答としては open, close を管理するのが一番わかりやすそう。一応この解答ならさくっと書けるようにはなった。stack を使ってループに直すのも簡単。
*   他の人の解答にある generator だったり for loop だったりはまだまた。
