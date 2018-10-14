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

* HybridAnalysisのApiKey設定
HybridAnalysisのサイトからApiKey, ApiSecretを取得する。
参考：https://www.hybrid-analysis.com/docs/api/v2
取得したApiKey, ApiSecretを VxAPIのconfig.pyに設定する。
# config.pyはconfig_tpl.pyをconfig.pyにリネームする

* VirusTotalのApiKey設定
VirusTotalのサイトからApiKeyを取得する。
参考：https://www.virustotal.com/fr/documentation/public-api/
取得したApiKeyをmail_attach_analyzer.py の170行目に設定する。



# run
Pythonプログラムの実行
