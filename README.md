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

* Python3環境設定

Python3ライブラリをインストール。

    
sudo apt install python3-pip
pip3 install requests BeautifulSoup4
    

# 実行

* JC3サイトからマルウェアメール添付ファイル例を使用して情報収集
python3 mail_attach_analyzer.py -jc3

* CSVファイルを読み込み情報収集
python3 mail_attach_analyzer.py -csv [CSV_FILE_NAME]
