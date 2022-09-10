# minesweeper

## 概要
2022年クラウドアプリ開発入門講座を受講し，アプリ開発及び報告会を行うこととなった．その成果物をとして今回は，マインスイーパ等の簡単なゲームをまとめたサイトを作る．

## 環境
- python 3.7.10
- Flask 2.0.2
- ブラウザ Google Chrome
## 環境内容
- ローカル： http://127.0.0.1:5000/
- デプロイ： https://minesweeper.azurewebsites.net/

## ローカル環境構築方法

### 1.作業ディレクトリを作成


```
# コマンドプロンプトからプロジェクトディレクトリを作成する

mkdir myproject
cd myproject

# git があるか確認
git --version

# git cloneを実行
git clone https://github.com/kawaguchi880/test_repo.git

# vscodeで開く
cd test_repo
code .

# Flaskパッケージの取得
# ※python 3.7.10を予めインストールしておく
# vscodeのターミナル上 cmdではなく，powershellで実行！
py -m venv .venv
.venv\Scripts\Activate.ps1

# requirements.txtから依存関係等をインストールする
pip install -r requirements.txt

# pip list でインストールされたものを確認できる
# pip をバージョンをアップグレードしたいなら，，↓↓↓
pip install --upgrade pip

# 環境変数を設定し，アプリを実行
$env:FLASK_ENV="development"
flask run
```

