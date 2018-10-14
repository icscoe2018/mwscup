# mwscup 2018 事前課題

# Description
メールの添付ファイルのファイル名を用いてマルウェア情報を取得するツール。
HybridAnalysis, VirusTotalから情報を収集。
メール添付ファイルのファイル名はJC3サイトからマルウェアのファイル名事例を使用すること、およびCSVファイルを用意してファイル名を読み込むことが可能。

# ツール環境設定

* VxAPIダウンロード
実行に必要なVxAPIライブラリをダウンロードしUbuntuLinux上の任意のディレクトリに展開。
https://github.com/PayloadSecurity/VxAPI

* 本ツールダウンロード
本Githubのmail_attach_analyzer.pyをダウンロードしVxAPIと同じディレクトリに展開。

* HybridAnalysisのApiKeyを取得し設定する
HybridAnalysisのサイトからApiKeyを取得する。
参考：https://www.hybrid-analysis.com/docs/api/v2
取得したApiKeyを mail_attach_analyzer.py のxxx行目に設定する。

API keyの取得

# run
Pythonプログラムの実行
