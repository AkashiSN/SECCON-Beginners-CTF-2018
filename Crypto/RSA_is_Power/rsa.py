#!/usr/bin/env python3

#
# Compute the RSA cipher
#

import gmpy2,binascii

n = int(input('n:'))
e = int(input('e:'))
p = int(input('p:'))
q = int(input('q:'))
c = int(input('c:'))

d = gmpy2.invert(e,(p-1)*(q-1))

m = pow(c,d,n)

flag = binascii.unhexlify(format(m, 'x')).decode()

print("FLAG: {}".format(flag))
