OCamlの単項演算子の結合順序がPythonとは異なるため、SymPyで計算した結果をそのまま使うと問題が生じるかもしれない。
SymPyを使うときは確認してから使うこと。
現時点でOCamlコードに書かれた式が正しいことは確認した。

Pythonの式をOCamlの式へ自動で変換するいい仕組みがあればいいのだが。

## シミュレーションの作成

報告書のシミュレーションを作るよ。
10次元の分布を生成するのは不可能なので、手先の質量だけ不確かである場合、すなわち1次元の不確かさに対する動的可操作性を考えよう。
