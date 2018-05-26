import requests

url = "http://goods.chall.beginners.seccon.jp/items.php?minstock="
r = requests.get(url+"\'")
print(r.text)