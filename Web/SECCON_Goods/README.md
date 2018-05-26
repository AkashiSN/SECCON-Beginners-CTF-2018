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

