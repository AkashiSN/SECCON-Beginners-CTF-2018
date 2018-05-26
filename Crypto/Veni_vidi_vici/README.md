# [Warmup] Veni, vidi, vici

## Question

[veni_vidi_vici.zip](veni_vidi_vici_e95fe3cb7932bfe5c017f018940652d0c0876fc8.zip)

## Answer

```bash
$ cat << EOF >> $HOME/.env
alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
EOF
$ cat part1 | rot13
The first part of the flag is: ctf4b{n0more
```

part2は[ROT encoder/decoder](http://theblob.org/rot.cgi?text=Lzw+kwugfv+hsjl+gx+lzw+xdsy+ak%3A+_uDskk%21usd_u)を使った

`ROT-8: The second part of the flag is: _cLass!cal_c`

part3は[Lunicode](https://lunicode.com/)を使った

`The third part of the flag is: Rypt0graphy}`

よって

`ctf4b{n0more_cLass!cal_cRypt0graphy}`