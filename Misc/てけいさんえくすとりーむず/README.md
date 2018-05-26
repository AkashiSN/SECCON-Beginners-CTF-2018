# てけいさんえくすとりーむず

## Question

てけいさんのプロのために作りました。
えくすとりーむなので300秒でタイムアウトします。

`$ nc tekeisan-ekusutoriim.chall.beginners.seccon.jp 8690`

## Answer

```bash
$ nc tekeisan-ekusutoriim.chall.beginners.seccon.jp 8690
Welcome to TEKEISAN for Beginners -extreme edition-
---------------------------------------------------------------
Please calculate. You need to answered 100 times.
e.g.
(Stage.1)
4 + 5 = 9
...
(Stage.99)
4 * 4 = 869
[!!] Wrong, see you.
---------------------------------------------------------------
(Stage.1)
770 + 553 =
```

計算するプログラムを書く

[solve.py](solve.py)

```python
#!/usr/bin/env python2.7

from netcat import Netcat

nc = Netcat('tekeisan-ekusutoriim.chall.beginners.seccon.jp', 8690)

nc.read_until('-\n(')

for i in range(100):
	nc.read_until('\n')
	s = nc.read_until('= ')[:-3]
	ans = eval(s)
	print(s +" = "+ str(ans))
	nc.write(str(ans)+'\n')
print(nc.read(100))
```

```bash
$ python2 solve.py
...
Congrats.
Flag is: "ctf4b{ekusutori-mu>tekeisann>bigina-zu>2018}"
```

`ctf4b{ekusutori-mu>tekeisann>bigina-zu>2018}`