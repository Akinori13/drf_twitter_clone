# drf_twitter_clone
## SetUp
### スーパーユーザーの作成
```
python manage.py createsuperuser
```
サンプル
| 項目           | 内容              |
| -------------- | ----------------- |
| メールアドレス | admin@example.com |
| 名前           | admin             |
| パスワード     | Password0622      |

### 起動
```
python manage.py runserver
```

### POSTMAN
下記をPOSTMANの'http://127.0.0.1:8000/api/accounts/token/'
```
pm.collectionVariables.set("Access",  pm.response.json()["access"]);
pm.collectionVariables.set("Refresh", pm.response.json()["refresh"]);
```

### CURL
curlではなくHTTPieの利用も検討

### Logging
- クエリ履歴：debug_db.log
- サーバー履歴：debug_server.log

### DB
VSCodeのSQLiteViewerを使用することでdb.sqlite3の内容を確認可能。

## Login機能のガイド
以下はcurlでガイドするが、POSTMANやHTTPieの利用も可能。
### トークン発行
```
curl -X POST "http://127.0.0.1:8000/api/accounts/token/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{"email": "YourEmail@example.com", "password": "YourPassword"}'
```

### トークン再取得
```
curl -X POST "http://127.0.0.1:8000/api/accounts/token/refresh/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{"refresh": "YourRefreshToken"}'
```

### トークン無効化
'''
curl -X POST "http://127.0.0.1:8000/api/accounts/token/blacklist/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{"refresh": "YourRefreshToken"}'
'''