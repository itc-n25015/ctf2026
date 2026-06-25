# Apache Webサーバ構築マニュアル（Basic認証付き）

## 1. Apacheのインストール

sudo apt update
sudo apt install apache2 apache2-utils -y

## 2. Apacheの起動

sudo systemctl enable apache2
sudo systemctl start apache2

## 3. Basic認証ユーザの作成

sudo htpasswd -c /var/www/html/.htpasswd testuser

## 4. .htaccessの作成

sudo vi /var/www/html/.htaccess

記述内容

AuthType Basic
AuthName "Restricted Area"
AuthUserFile /var/www/html/.htpasswd
Require valid-user

## 5. Apache設定変更

/etc/apache2/apache2.conf を編集する。

<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride None 
	Require all granted
</Directory>
<Directory /var/www/html/>
	AllowOverride AuthConfig
</Directory>

## 6. Apache再起動

sudo systemctl restart apache2

## 7. 動作確認

ブラウザでアクセスする。

http://192.168.122.204

認証画面が表示されれば成功。


# FTPサーバ（vsftpd）構築マニュアル

## 1. vsftpdのインストール

sudo apt update
sudo apt install vsftpd -y

## 2. サービスの起動

sudo systemctl enable vsftpd
sudo systemctl start vsftpd

## 3. 動作確認

サービスの状態を確認する。

sudo systemctl status vsftpd

## 4. FTP接続確認

クライアントから接続する。

ftp 192.168.122.204

ログインできれば構築成功。

# Telnetサーバ構築マニュアル

## 1. Telnet関連パッケージのインストール
sudo apt update
sudo apt install tenlnet xinetd -y

## 2. xinetdの起動

sudo systemctl enable xinetd
sudo systemctl start xinetd

## 3. Telnet設定ファイル作成

sudo vi /etc/xinetd.d/telnet

以下の内容を記述する。

service telnet
{
 disable     = no
    flags       = REUSE
    socket_type = stream
    wait        = no
    user        = root
    server      = /usr/sbin/telnetd
    log_on_failure += USERID
}

## 4. xinetd再起動

sudo systemctl restart xinetd

## 5. 動作確認

サービス状態を確認する。

sudo systemctl status xinetd

## 7. Telnet接続確認

クライアントから接続する。

telnet 192.168.122.204

ログイン画面が表示されれば成功。



