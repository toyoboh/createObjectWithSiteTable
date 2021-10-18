## 使用方法  
　当該フォルダに移動し、以下コマンド実行  
```
$ python index.py
```

## 説明  
　以下サイトの「減価償却資産の償却率表」の表のデータを取得し  
　JavaScriptで使用できるオブジェクト形式に加工、及び出力をする  
　【参照サイト】  
　　http://tool.yurikago.net/644/yurikago/2012shokyakuritsu.html  

## 使用技術  
　Python 3.8.0（3.9.0以降だとpandasがまだ使えないみたい）  

## 環境構築（Mac用）  
　●Homebrewインストール  
　　・バージョン確認（not foundならインストール要）  
```
$ brew -v
```

　　・インストール  
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

　●pyenvインストール  
　　・バージョン確認（not foundならインストール要）  
　　　`$ pyenv -v`  

　　・インストール  
　　　`$ brew install pyenv`  

　　・pyenvの設定（echoの部分はviで ~/.zshrcに書いてもいい）  
　　　【zshの場合】  
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc  
    $ echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.zshrc  
    $ echo 'eval "$(pyenv init -)"' >> ~/.zshrc  
    $ source ~/.zshrc  

　●Pythonのインストール  
　　・pyenvでインストール可能なバージョンの一覧を確認  
　　　`$ pyenv install --list`  

　　・Pythonのインストール（今回はpandasを使いたいので、3.8.0を使う）  
　　　`$ pyenv install 3.8.0`  

　　・pyenvによって管理されているものの確認（インストールしたバージョンが表示される）  
　　　`$ pyenv versions`  

　　・Pythonのバージョンの指定  
　　　`$ pyenv global 3.8.0`  

　　・Pythonのバージョン確認  
　　　`$ python --version`  

## 使用するライブラリのインストール方法  
　`$ pip install pandas lxml html5lib beautifulsoup4`  

　【関連サイト】  
　　https://note.nkmk.me/python-pandas-web-html-table-scraping/  

　【インストール時エラーの関連サイト】  
　　・macOS Big Surアップデート後のエラーの場合  
　　　　https://qiita.com/Butterthon/items/e7d1f379c828b41f3e19  

　　・pyenv installでwarning generated エラー発生時  
　　　　https://harucharuru.hatenablog.com/entry/2020/11/16/205232  

　　・pandas使用時に"lzma"が入っていないというwarningが発生した場合  
　　　　https://zenn.dev/grahamian/articles/f292163325653dbe2c42  
