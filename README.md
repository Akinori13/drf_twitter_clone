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
pm.collectionVariables.set("Access",   "Bearer  " + pm.response.json()["access"]);
pm.collectionVariables.set("Refresh", pm.response.json()["refresh"]);
```

### CURL
curlではなくHTTPieの利用も検討

### Logging
- クエリ履歴：debug_db.log

### DB
VSCodeのSQLiteViewerを使用することでdb.sqlite3の内容を確認可能。

## Login機能のガイド
以下はcurlでサンプルのガイドを行うが、POSTMANやHTTPieの利用を推奨。

注意事項としてLoginRequiredなAPIに対しては`Authorization: Bearer YoureAccessToke`となるようにする。

### トークン発行
#### Request
```
curl -X POST "http://127.0.0.1:8000/api/accounts/token/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{"email": "YourEmail@example.com", "password": "YourPassword"}'
```
#### Response
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjUzNjY5MiwiaWF0IjoxNjc5OTQ0NjkyLCJqdGkiOiI5M2Y2NDcwYjZiYTc0NjhkODY1MTQ1MjhlZGFjMDI4NyIsInVzZXJfaWQiOiJlODVmNTRlNC0yMmYzLTRhMTAtOGI4Zi0yNmRhNzFlODEzYzkifQ.IkxPDnvb4pgKqi6nUfViME4wTWsOzXhHHJoyzIl6rOE",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5OTQ4MjkyLCJpYXQiOjE2Nzk5NDQ2OTIsImp0aSI6IjBjZjdiNDM5NzFlZDQ2MzM5NmRmZDhjMGZiMGZkMzZhIiwidXNlcl9pZCI6ImU4NWY1NGU0LTIyZjMtNGExMC04YjhmLTI2ZGE3MWU4MTNjOSJ9.cI2LUCTy3H4LczDmc0wcvPQdOnSn8NvRWSB6B53WFp4"
}
```

### トークン再取得
#### Request
```
curl -X POST "http://127.0.0.1:8000/api/accounts/token/refresh/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{"refresh": "YourRefreshToken"}'
```
#### Response
```
{
    "access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5OTQ5MTM1LCJpYXQiOjE2Nzk5NDQ2OTIsImp0aSI6ImI3OTUxZWY0NmNjMDQ0OTdiNTkwNGY1YmRhM2RiYmNmIiwidXNlcl9pZCI6ImU4NWY1NGU0LTIyZjMtNGExMC04YjhmLTI2ZGE3MWU4MTNjOSJ9.KFscyVruRoBs9sV27kuxizid8l7SMs7g_oDFopkyQrE","refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjUzNzUzNSwiaWF0IjoxNjc5OTQ1NTM1LCJqdGkiOiI4NDYyNGJlNDVmMDc0NDc4ODE5MTlmOTZiOGJjMjVlYiIsInVzZXJfaWQiOiJlODVmNTRlNC0yMmYzLTRhMTAtOGI4Zi0yNmRhNzFlODEzYzkifQ.rUewXF9KND4G1U_8P72Q94TMSLBQHdEYGekUON47yNc"
}
```

### トークン無効化
#### Request
'''
curl -X POST "http://127.0.0.1:8000/api/accounts/token/blacklist/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{"refresh": "YourRefreshToken"}'
'''
#### Response
```
{}
```

### ユーザー登録
#### Request
'''
curl -X POST "http://127.0.0.1:8000/api/accounts/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{
        "email": "sampleUser@example.com",
        "username": "SampleUser",
        "password": "Password0622"
    }'
'''
#### Response
```
{
    "email":"sampleUser@example.com",
    "username":"SampleUser"
}
```

### ユーザー一覧
#### Request
'''
curl "http://127.0.0.1:8000/api/accounts/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -H  "Authorization: Bearer YoureAccessToken"
'''
#### Response
```
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "0f2f6abf-5eb4-4c05-b83e-2ac145b57041",
            "username": "SampleUser",
            "joined_at": "2023-03-28T04:35:42.454372+09:00"
        }
    ]
}
```

### ユーザー取得
#### Request
'''
curl "localhost:8000/api/accounts/{{user_id}}/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -H  "Authorization: Bearer YoureAccessToken"
'''
#### Response
```
{
    "id": "0f2f6abf-5eb4-4c05-b83e-2ac145b57041",
    "username": "SampleUser",
    "joined_at": "2023-03-28T04:35:42.454372+09:00"
}
```

### ユーザー更新
#### Request
'''
curl -X PATCH "localhost:8000/api/accounts/{{user_id}}/" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -H  "Authorization: Bearer YoureAccessToken"
    -d '{
        "username": "SampleUserB"
    }'
'''
#### Response
```
{
    "id":"0f2f6abf-5eb4-4c05-b83e-2ac145b57041",
    "email":"sampleUser@example.com",
    "username":"SampleUserB"
}
```