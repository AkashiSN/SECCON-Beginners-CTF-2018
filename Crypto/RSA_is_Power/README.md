# RSA is Power

## Question

```plain
N = 97139961312384239075080721131188244842051515305572003521287545456189235939577
E = 65537
C = 77361455127455996572404451221401510145575776233122006907198858022042920987316
```

## Answer

[YAFU](https://ja.osdn.net/projects/sfnet_yafu/)で`N`を因数分解してみる

```bash
$ yafu "factor(97139961312384239075080721131188244842051515305572003521287545456189235939577)" -v -threads 32


05/26/18 20:33:57 v1.34.5 @ server, System/Build Info:
Using GMP-ECM 6.4.4, Powered by GMP 5.1.1
detected Intel(R) Xeon(R) CPU E5-2623 v3 @ 3.00GHz
detected L1 = 32768 bytes, L2 = 10485760 bytes, CL = 64 bytes
measured cpu frequency ~= 2996.525010
using 20 random witnesses for Rabin-Miller PRP checks

===============================================================
======= Welcome to YAFU (Yet Another Factoring Utility) =======
=======             bbuhrow@gmail.com                   =======
=======     Type help at any time, or quit to quit      =======
===============================================================
cached 78498 primes. pmax = 999983


>> fac: factoring 97139961312384239075080721131188244842051515305572003521287545456189235939577
fac: using pretesting plan: normal
fac: no tune info: using qs/gnfs crossover of 95 digits
div: primes less than 10000
rho: x^2 + 3, starting 1000 iterations on C77
rho: x^2 + 2, starting 1000 iterations on C77
rho: x^2 + 1, starting 1000 iterations on C77
pm1: starting B1 = 150K, B2 = gmp-ecm default on C77
fac: setting target pretesting digits to 23.69
fac: sum of completed work is t0.00
fac: work done at B1=2000: 0 curves, max work = 30 curves
fac: 30 more curves at B1=2000 needed to get to t23.69
ecm: 30/30 curves on C77, B1=2K, B2=gmp-ecm default
fac: setting target pretesting digits to 23.69
fac: t15: 1.00
fac: t20: 0.04
fac: sum of completed work is t15.18
fac: work done at B1=11000: 0 curves, max work = 74 curves
fac: 74 more curves at B1=11000 needed to get to t23.69
ecm: 74/74 curves on C77, B1=11K, B2=gmp-ecm default
fac: setting target pretesting digits to 23.69
fac: t15: 7.17
fac: t20: 1.04
fac: t25: 0.05
fac: sum of completed work is t20.24
fac: work done at B1=50000: 0 curves, max work = 214 curves
fac: 149 more curves at B1=50000 needed to get to t23.69
ecm: 149/149 curves on C77, B1=50K, B2=gmp-ecm default, ETA: 0 sec
fac: setting target pretesting digits to 23.69
fac: t15: 28.45
fac: t20: 8.13
fac: t25: 0.74
fac: t30: 0.05
fac: sum of completed work is t23.72

starting SIQS on c77: 97139961312384239075080721131188244842051515305572003521287545456189235939577

==== sieve params ====
n = 79 digits, 260 bits
factor base: 36160 primes (max prime = 913337)
single large prime cutoff: 77633645 (85 * pmax)
allocating 7 large prime slices of factor base
buckets hold 2048 elements
using SSE4.1 enabled 32k sieve core
sieve interval: 10 blocks of size 32768
polynomial A has ~ 10 factors
using multiplier of 17
using SPV correction of 21 bits, starting at offset 34
using SSE2 for x64 sieve scanning
using SSE2 for resieving 13-16 bit primes
using SSE2 for 8x trial divison to 13 bits
using SSE4.1 and inline ASM for small prime sieving
using SSE2 for poly updating up to 15 bits
using SSE4.1 for medium prime poly updating
using SSE4.1 and inline ASM for large prime poly updating
trial factoring cutoff at 89 bits

==== sieving in progress (32 threads):   36224 relations needed ====
====            Press ctrl-c to abort and save state            ====
42718 rels found: 20803 full + 21915 from 211316 partial, (21647.05 rels/sec)

sieving required 74715 total polynomials
trial division touched 3933801 sieve locations out of 48965222400
QS elapsed time = 10.7339 seconds.

==== post processing stage (msieve-1.38) ====
begin with 232119 relations
reduce to 61668 relations in 2 passes
attempting to read 61668 relations
recovered 61668 relations
recovered 41980 polynomials
freed 17 duplicate relations
attempting to build 42701 cycles
found 42701 cycles in 1 passes
distribution of cycle lengths:
   length 1 : 20800
   length 2 : 21901
largest cycle: 2 relations
matrix is 36160 x 42701 (6.2 MB) with weight 1273677 (29.83/col)
sparse part has weight 1273677 (29.83/col)
filtering completed in 4 passes
matrix is 25674 x 25738 (3.9 MB) with weight 819682 (31.85/col)
sparse part has weight 819682 (31.85/col)
saving the first 48 matrix rows for later
matrix is 25626 x 25738 (3.3 MB) with weight 670513 (26.05/col)
sparse part has weight 598982 (23.27/col)
matrix includes 64 packed rows
using block size 10295 for processor cache size 10240 kB
commencing Lanczos iteration
memory use: 3.0 MB
lanczos halted after 407 iterations (dim = 25624)
recovered 16 nontrivial dependencies
Lanczos elapsed time = 1.2800 seconds.
Sqrt elapsed time = 0.0400 seconds.
SIQS elapsed time = 12.0546 seconds.
pretesting / qs ratio was 1.40
Total factoring time = 28.9849 seconds


***factors found***

P39 = 299681192390656691733849646142066664329
P39 = 324144336644773773047359441106332937713

ans = 1
```

できた!

[rsa.py](rsa.py)

```bash
$ ./rsa.py
n:97139961312384239075080721131188244842051515305572003521287545456189235939577
e:65537
p:299681192390656691733849646142066664329
q:324144336644773773047359441106332937713
c:77361455127455996572404451221401510145575776233122006907198858022042920987316
FLAG: ctf4b{5imple_rs4_1s_3asy_f0r_u}
```

`ctf4b{5imple_rs4_1s_3asy_f0r_u}`