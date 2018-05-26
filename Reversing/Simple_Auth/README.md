# [Warmup] Simple Auth

## Question

認証に使われているパスワードを探せ！

[Simple_Auth.zip](Simple_Auth_d6d1615ec0ca18b0e911467b58c0d8e0a4b306fa.zip)

## Answer

`ltrace`したらなんか出てきた

```bash
$ ltrace ./simple_auth
__libc_start_main(0x400792, 1, 0x7ffede46afd8, 0x400830 <unfinished ...>
printf("Input Password: ")                                                                                                        = 16
__isoc99_scanf(0x4008c5, 0x7ffede46aec0, 0, 0Input Password: hoge
)                                                                                    = 1
strlen("hoge")                                                                                                                    = 4
strlen("ctf4b{rev3rsing_p4ssw0rd}f~O\340\177")                                                                                    = 30
puts("Umm...Auth failed..."Umm...Auth failed...
)                                                                                                      = 21
+++ exited (status 0) +++
```

`ctf4b{rev3rsing_p4ssw0rd}`