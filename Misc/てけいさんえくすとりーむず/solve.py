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