# 3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Comments

### step1

*   Sliding window であることはカテゴリからわかっていたので、それで考えた。
*   `characters.remove(s[left])` `left += 1` をループの中と外で書いているのどうなの (`s[left] != s[right]` の条件だから、`s[left] == s[right]` の分を除く処理が必要)。
*   `while left < right ` はなくても動く (set に追加された文字であることは確実なのでループはこの条件を満たす前に止まる)。

### step2

*   https://github.com/hayashi-ay/leetcode/pull/47/files
*   シンプルに書き直す (`Solution1`)。
    *   if の条件と while の条件がタブっている。また `while s[right] in seen:` とすれば、step1 のようにループ内外で同じ処理は不要
*   > 登場した文字のインデックスも覚えておくとleftの移動が飛び飛びになる場合にちょっと効率的。
    *   これは考えていなかった。確かに。
    *   インデックスを記憶する版を書いてみたが、WA (`Solution2WA`)。set と同様にdel していけばいいんじゃないかと思って書いたけど、よく考えたら、最後の a に到達したとき、left が最初の a まで戻ってしまう。ので上記にあるように left がより右側にある場合は left の位置を優先 (substring をリセット) する必要がある (`Solution2_1`)。
    *   まずはインデックスを使わない方法で書くのが期待値かな、と感じる。
    *   left = max(left, ...) しないといけないの、どうやったら気づけたんだろう。最初解答を見たとき、これいるんだっけ？と思って、やらずに submit してからテストケースをじっくり眺めてようやく気づいた。

```
s="abba"
left=0, right=0, max_len=1
left=0, right=1, max_len=2
left=2, right=2, max_len=2
left=1, right=3, max_len=3
```

*   https://github.com/olsen-blue/Arai60/pull/49#discussion_r2005295464
    *   `left = max(left, seen_index.get(s[right], -1) + 1)` で一応条件分岐をなくせる (`Solution2_2`)。`s[right]` が seen にない場合は -1 (つまり length が 0) になれば影響がない。
    *   オプションや発想として出てくるようにはしたいかなという感じ？
*   sliding window、window が伸び縮みしながら動くイメージのほか、左側をリセットする (右側に揃える) ケースがあるのは選択肢として頭に置いておきたい。

### step3

*   最初インデックス使わないパターンで書いたが、さらっと書けそうだったので残りはインデックス使うパターンで練習した。
*   1:40 (`Solution1`)-> 2:30 (`Solution2`) -> 1:30 (`Solution2`)
