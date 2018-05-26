# [Warmup] Greeting

## Question

ようこそ！

[http://greeting.chall.beginners.seccon.jp](http://greeting.chall.beginners.seccon.jp)

## Answer

[http://greeting.chall.beginners.seccon.jp](http://greeting.chall.beginners.seccon.jp)
にアクセスすると

![Clipboard01.png](Clipboard01.png)

```php
$username = htmlspecialchars($_POST['name'], ENT_QUOTES, "UTF-8");

// 管理者でログインできる？
  if($username === "admin") {
    $username = "偽管理者";
  }
} elseif(isset($_COOKIE['name'])) {
  $username = htmlspecialchars($_COOKIE['name'], ENT_QUOTES, "UTF-8");
} else {
  $username = "ゲスト";
}
```

ポストで受け取ったデータを`_COOKIE`で上書きしてるので`admin`を送信してから再読込ではなくもう一度アクセスし直すとフラグが出る

![Clipboard01.png](Clipboard01.png)

`ctf4b{w3lc0m3_TO_ctf4b_w3b_w0rd!!}`
