# 323. Number of Connected Components in an Undirected Graph

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

## Comments

### step1

*   islands の問題と似たようなのかなーと思ったが、graph を作るところから始まるのか。
*   adjacency list と adjacency matrix どっちにしようか考える
*   どっちでも解けると思うけど edge が少ないと matrix が sparse になるので、list でいい気がする。index でのアクセスは matrix の方が速いけど今回はどちらにしても辺をすべて舐めていくことになるので、あまり違いがないと思う。
*   Union Find は明らかに使えるんだけど、ちょっと実装に自信がないので DFS や BFS で解くことを考える。
*   初見から 14:00 くらいで書き上げた。でもテストケースを脳内で走らせてみると、[[2, 0], [2, 1]] のようなインプットで動かないことに気づく。この時点で 16:00 くらい (`SolutionWA`)。つらい。
*   一旦仕切り直して落ち着いて考えてみる。この方法だと DFS して、unique_components += 1 したタイミングですべての connected node を visited にしておかないと重複カウントが出る。というわけで 3:00 くらい？ (計測なし) で DFS で書き直した。Accepted (`SolutionAccepted`)

### step2

*   他の解答見てみる
    *   https://github.com/hayashi-ay/leetcode/pull/37/files
        *   方向性概ね同じ。Union Find 使った実装ものせている。
    *   https://github.com/Mike0121/LeetCode/pull/35/files
*   Union Find 使ってみようかなと思った。
    *   https://github.com/ryosuketc/leetcode_arai60/pull/17/files
*   Union Find 実装してみた。16:00 くらいで見直し含めて実装したんだけど、self のつけ忘れとかでちょいちょいバグ。
*   Union FInd の実装は正しかったのだが、ただもともとは `unique_components = 0` から始めて、union が成功したら 1 足すという謎の実装にしていたせいで WA。他の解答見て間違いに気づいたので修正

### step3

*   本来は dfs で解きたい気はするが、幅を広げるために Union Find を練習してみる。実際の面接だと、path compression や union by rank の実装はせずに最初書いて、時間余ったら足す、というほうがいいかも。
*   9:40 (typoあり) -> 5:30 -> 5:00

ここの処理

```python
        if self._rank[parent1] < self._rank[parent2]:
            self._parents[parent1] = parent2
            self._rank[parent2] += self._rank[parent1]
        else:
            self._parents[parent2] = parent1
            self._rank[parent1] += self._rank[parent2]
```

こんな感じにしようか迷ったけど、rank が同じ場合、最初の引数の parent1 が返るので意図した挙動にならない。

https://docs.python.org/3/library/functions.html#max
> If multiple items are maximal, the function returns the first one encountered.

```python
        # Wrong
        smaller_parent = min(parent1, parent2, key=lambda x: self._rank[x])
        bigger_parent = max(parent1, parent2, key=lambda x: self._rank[x])
```

これは動くが、きもい。わざわざ三項演算子いらない…

```python
        smaller_parent = min(parent1, parent2, key=lambda x: self._rank[x])
        bigger_parent = parent2 if smaller_parent == parent1 else parent1
```

これも動くが、これなら最初のコードでよい (smaller, bigger にアサインしなくても…)

```python
        if self._rank[parent1] < self._rank[parent2]:
            smaller_parent = parent1
            bigger_parent = parent2
        else:
            smaller_parent = parent2
            bigger_parent = parent1
        self._parents[smaller_parent] = bigger_parent
        self._rank[bigger_parent] += self._rank[smaller_parent]
```
