# PyRq
PythonでHTTPリクエストを送りやすくするためのライブラリです

## 依存関係
` requests `

## インストール
> cURLを使用してインストール  

```
$ pip install curl https://riysan.github.io/PyRq/pkg/pyrq-1.0.0.tar.gz 
```
  

> Gitを使用してインストール  

```
$ pip install git+https://github.com/Riysan/PyRq.git 
```

## リファレンス
### 仕様
urlが空の場合 ` null ` を返します
### 基本文

```python
import pyrq

pyrq.text("http://example.com")

#又は

import pyrq as r #エイリアスを付ける事で短くできます

r.text("http://example.com")
```

### TXETの取得
```python
pyrq.text("**ここに取得先のURLを入力**")
```

### JSONの取得
```python
pyrq.json("**ここに取得先のURLを入力**")
```
オブジェクトがレスポンスされます

### 短縮URLの生成
ついでに付けてみたという感じです。  
[LimeleAPI](https://github.com/Riysan/LimeleAPI/) を利用しています。
```python
pyrq.limele("**ここに短縮したいURLを入力**")
```
