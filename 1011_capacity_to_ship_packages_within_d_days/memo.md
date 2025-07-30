# 1011. Capacity To Ship Packages Within D Days

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

## Comments

### step1

*   最初の解答 (`Solution1WA`)
    *   14:00 くらい？ 脳内でテスト走らせてみて行けそうな気がした
    *   submit して WA。print debug してみて問題にはすぐ気付いた。脳内に走らせたときに自分で気づきたかった。
        *   `if remaining_capacity - weight > 0:` は等号含む (remaining は 0 になってよい)
        *   weight > capacity となるケースを考えていなかった…
    *   テストケースを走らせるとき、色々な入力 (今回だと weight が capacity をそもそも超えているとか) を考慮できるようにしなければ。。前より意識はあるが、漏れがある。
*   `Solution2` に修正して 21:00 くらい
*   get_days_to_ship が days を超える時点で return inf とかしてもいいんだけど、`get_days_to_ship(capacity)` という signature には合わない気がした (かかる日数が長くても返してほしい)。もし days を超えた時点で return するなら、`get_days_to_ship(capacity, days_limit=days)` みたいな signature にして limit があるのを明記したい。
*   get_days_to_ship の for 内部の処理はもうちょっとシンプルに書けそう。
*   while を 2 重にしたほうが手でやる捜査には近いかも。weight を順番に、cap の許す限り詰め込む。いっぱいになったら新しい cap を用意してまた詰め始める。
*   

### step2

*   他の解答を見る前に while で書き直したら TLE (無限ループ) して 40:00 くらい溶かした (`Solution1TLE`)。
    *   結局、 `weights[i] > capacity` のとき、`capacity_left - weights[i] >= 0` によって内側の while を抜けるけど、i が increment されないので外を抜けられないという話。
    *   `Solution2AC` のように外の while でチェックすればよい
*   なぜこういうエラー起こしたんだろう。インタビューでこれ (無限ループになりますね、と言われてデバッグに溶かす) したらまあ詰むだろう…
    *   内側のループを抜けない可能性ばかりを考えていたかも？？
*   というかそもそも `low = 1` から始めているのが筋が悪い… `low = max(weights)` なら step1, 2 ともこういう問題は起きなかった。high をどうすればいいかというのは冒頭に考えていたけど、low をどうすべきかというのはちゃんと考えていなかった。
    *   最終直したのが `Solution3AC`
*   https://github.com/fuga-98/arai60/pull/44/files
    *   `can_ship` とかで、指定の days 以内に ship できるかの bool 返す関数はありかも。
        *   `Solution4AC`: 悪くはないかな？メインの関数がややシンプルになる。余分な計算も出ないしこのほうがいいかも。
    *   bisect を使った実装もあるようだ
        *   `return bisect_left(range(sum(weights) + 1), True, key=can_ship)`
        *   一応 step1 の時点で、FFFFTTTT みたいな配列の最初の T を返せばいいのねという発想はあり、まあ bisect_left は使えるでしょうという感覚はあった
### step3

*   7:00 -> 5:00 -> 4:15
*   何回か書いているうち、やはり while より for の方が個人的には書きやすいと感じた。
*   for の中の処理は、手でやるときの操作を明確にイメージしてから書くと違和感がなかった
    *   容量 capacity の箱を 1 つ用意します。箱は days 個あります。
    *   重さ weight の荷物を順番に入れていきます。
    *   その荷物が、眼の前の箱に入るなら入れます。
    *   入らない場合
        *   新しい箱を用意します。
        *   新しい箱にその荷物を入れます。
        *   使った箱数をカウントします (使った箱カウントを1 箱増やす or 箱の残り数を減らす。今の実装は前者)
        *   まだ荷物がある状態で箱が途中でなくなったら、積みきれなかったことを報告します。
        *   すべての荷物を詰め終わったら完了を報告します。
