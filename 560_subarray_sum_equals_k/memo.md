# 560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/description/

## Comments

### step1

*   最初 subarray の定義がわからなくて問題文にある例が理解できなかった。
    *   **連続する**要素の配列 (長さが 1 も含む) ということだと理解
*   二重ループで回して、途中で sum_starting_from_i が k になったらそのループやめて…とか考えたけど、nums[i] はゼロ及び負の数もあるので、全走査しないと正しい答えが出ない。
*   TLE しそうだけど全走査したら答え出るよね、で書いた。案の定 TLE した (`Solution`)。
*   ここまでで 7:30 くらい。
*   subarray、というかそのループで和を求めているので、累積和使えばいいのかな？と思いつくけど、具体的な手順にまで落とし込めなかった。

### step2

*   LeetCode の答え (Approach2) 見て `Solution2` を実装した。
*   結局 TLE した。Java だと通るけど、Python だと TLE するっぽい (自分のコードが間違ってなければ)
*   というか `Solution`  も `Solution2` も O(N^2) で本質的に同じじゃない？ (`Solution2`  は累積和の配列を使っているけど、`Solution` は `sum_starting_from_i` の整数を使って O(1) spaace にしている)
    *   と思って LeetCode の Approach3 見たらその通りだった。
    *   つまり自分で考えた最初の解法 (`Solution`)、実際累積和の考え方を使っている (気づけば当たり前なんだけど、累積和といえば配列というバイアスがあった)
*   となると、O(N^2) の解法だと Python ではどう頑張っても TLE するのか…
    *   以下、時間計算量、空間計算量について のセクションを参照
*   他の人の解答見てみる
    *   https://github.com/potrue/leetcode/pull/16/files
        *   冒頭見てみたけど O(N) の解法から入っているので自分が求めているものではなかった
    *   https://github.com/Satorien/LeetCode/pull/16/files
        *   O(N^2) から始めて自分と同じ過程を辿っているが、O(N) の解法理解についてはあまりコメントがない
    *   https://github.com/fuga-98/arai60/pull/17/files
        *   ここに書いてある思考プロセスがわかりやすかった
        *   cumulative_sum は prefix_sum とも言うのを知った。こっちのほうがスペルしやすい
            *   https://en.wikipedia.org/wiki/Prefix_sum
*   標高の話: https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.bp0g0ai41eln
*   accumulate
    *   https://docs.python.org/ja/3.13/library/itertools.html#itertools.accumulate
    *   itertools は色々便利なのもあるし知っといてもいいかも

### step3

*   標高の話でもまだしっくりこない…
*   NeetCode の解答で少しわかった気がする
    *   `k = 3`, `[1, 1, 1, 1]` のような subarray を考えていいるとき、現在 `i = 3` にいるわけだが、考え方としては
        *   今 `[1, 1, 1, 1]` の subarray を考えています。
        *   `prefix_sum = 4` なので、 ここから `prefix_sum - k = 1` だけ除くことができれば、k = 3 の subarray を作れます。`prefix_sum` が 1 になる subarray はそれまでにいくつありましたか (`prefix_sum_to_count`)。
*   `prefix_sum_to_count[prefix_sum] += 1` するのは、`result` をアップデートした後。
    *   今現在見ている subarray は考慮しない (?)
        *   ここが微妙にしっくり来ていない気がする

## 時間計算量、空間計算量について

### Quote

https://github.com/ichika0615/arai60/pull/8#discussion_r1898337850

> 時間計算量からおおよその処理時間を推定することもできます。時間計算量の式に n の最大値を代入すると、おおよその計算ステップ数になります。この計算ステップ数を、各言語ごとの 1 秒あたりに処理可能な計算ステップ数で割ると、おおよその処理時間が出ます。
Python の場合は 1 秒あたり 100 万ステップ程度計算できます。この数字は、 CPU の動作周波数と、 1 クロック当たりの命令実行数、言語ごとの差から推定できます。 CPU の動作周波数は、最近のものですと、数 GHz = 数十億ヘルツになります。仮に 1 クロックに 1 命令実行できると仮定すると、 1 秒間に数十憶命令実行できます。また、 C/C++ といったオーバーヘッドの少ない言語ですと、 1 秒間に 1 ～ 10 億ステップ程度実行できます。 Python の場合、インタープリターのオーバーヘッドが大きいため、 1 秒間に 100 万ステップ程度処理できます。言語ごとの処理速度の差については、以下のページが参考になると思います。

*   https://github.com/niklas-heer/speed-comparison
*   https://benchmarksgame-team.pages.debian.net/benchmarksgame/box-plot-summary-charts.html

> 今回の場合は add() の処理時間が支配的です。 add() 1 回あたりの時間計算量は O(n log n) で、最大で 104 回呼ばれます。よって 10^4 * log 10^4 * 10^4 = 1.5 * 10^9 ステップくらいになると思います。 Python は 1 秒に 100 万ステップ = 1.0 * 10^6 ステップ程度処理できますので、 1.5 * 10^9 / 10^6 = 1.5 * 10^3 = 1500 秒程度かかることになります。
コードを書く前に、自分が書くコードの処理時間が長すぎないか、あらかじめ時間計算量から見積もっておくことをお勧めいたします。ただし、用途によっては処理時間が長くても問題ない場合もあります。かけられる処理時間は用途によって大きく変わります。ゲームのように 1 フレーム16.6 ms 以内に処理を終わらせなければならない場合もあれば、機械学習のように何日かけてもよい場合もあります。
また、実装内容により処理時間は大幅に変わります。また、 CPU の 1 クロック当たりの命令実行数を正確に見積もることは難しいです。そのため、上記の推定方法は、参考程度にとどめておくことをお勧めいたします。


### 時間計算量

今回の問題についていえば、

> 1 <= nums.length <= 2 * 10^4

という制約。O(n^2) なら 10^8、O(n^3) なら 10^12 ステップくらい。Python が 10^6 step / second くらい実行できるとすると、10^2 で 100 秒くらいかかる。C++ や Java ならいけそうだが、確かに Python では無理そう。

実行時間については実測する手段もある (https://github.com/ryosuketc/leetcode_arai60/pull/12#discussion_r2104988217)

### 空間計算量

```python
In [42]: a = 1

In [43]: sys.getsizeof(a)
Out[43]: 28

In [44]: l = [1, 2, 3]

In [45]: sys.getsizeof(l)
Out[45]: 88

In [46]: sys.getsizeof(l[0])
Out[46]: 28

In [47]: sys.getsizeof(l[1])
Out[47]: 28

In [48]: sys.getsizeof(l[2])
Out[48]: 28

In [49]: sys.getsizeof(10^100000000)
Out[49]: 28

In [50]: sys.getsizeof(10^1000000000000000000000000000000)
Out[50]: 40

In [51]: sys.getsizeof(10^1000000000000000000000000000000000000000000000000000000000000000000)
Out[51]: 56

In [52]: sys.getsizeof(10^10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
Out[52]: 68

In [53]: sys.getsizeof(10^100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
Out[53]: 76
```

```python
In [59]: sys.getsizeof('a')
Out[59]: 42
```

```python
In [62]: sys.getsizeof(1.234)
Out[62]: 24
```

```python
In [63]: a = [1]

In [64]: sys.getsizeof(a)
Out[64]: 64
```

*   getsizeof の output、最初 bit かと思ったけど byte だった (https://docs.python.org/3/library/sys.html#sys.getsizeof)。
    *   あれ、じゃあ整数 1 つでも 28 バイト消費している？ 64 bit int とかあるんだから、せいぜい 8 byte とかじゃないの。
*   Pytnon の整数は制限がないのは有名だけど、実際数字を大きくすると確保するメモリが大きくなっている
    *   https://zenn.dev/yukinarit/articles/afb263bf68fff2
    *   細かくは見てないけどこのへんで実装されているらしい: https://github.com/python/cpython/blob/72ec3193b5118a2ccc8be8bf03d7b74691c6a264/Objects/longobject.c
*   `list` のオーバーヘッドはそんなに大きくない (88 - 28 * 3 =  4 bytes)…と思ったけどこれは間違い。list を作ったとき、最小で 64 byte 消費するようだ (以降 1 要素ごと 8 byte)。
    *   だとするとたとえば 8 GB のメモリだと、10 億要素は保存できないくらいか。


公式ではないので参考程度だけど、これが参考になるかも: https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python

```
Bytes  type        scaling notes
28     int         +4 bytes about every 30 powers of 2
37     bytes       +1 byte per additional byte
49     str         +1-4 per additional character (depending on max width)
48     tuple       +8 per additional item
64     list        +8 for each additional
224    set         5th increases to 736; 21nd, 2272; 85th, 8416; 341, 32992
240    dict        6th increases to 368; 22nd, 1184; 43rd, 2280; 86th, 4704; 171st, 9320
136    func def    does not include default args and other attrs
1056   class def   no slots 
56     class inst  has a __dict__ attr, same scaling as dict above
888    class def   with slots
16     __slots__   seems to store in mutable tuple-like structure
                   first slot grows to 48, and so on.
```
