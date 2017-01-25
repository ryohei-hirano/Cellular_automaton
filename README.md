# Cellular_automaton
ROSでセルオートマトンのブログラムを動かします。

中央の円形で表示される5×5のセルはcount.pyによる値でランダムに変化します。残りのセルは以下ののルールによって変化します。

マスは□が死んでいる状態、■が生存している状態です。


以下のルールでセルの生死が変化します

1.死んでいるセルの周囲に、生きているセルが3セル存在すると、次世代で誕生

2.生きているセルの周辺に、2セルまたは3セルの生きているセルが存在すると、次世代でも生存

3.生きているセルの周辺に、4マス以上の生きているセルが存在すると、次世代で死滅

4.生きているセルの周辺に、生きているセルが1セル以下の場合。次世代で死滅

