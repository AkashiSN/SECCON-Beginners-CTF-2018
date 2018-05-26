# [Warmup] plain mail

## Question

[packet.pcap](packet.pcap)

## Answer

`wireshark`でみてやるとメールでパスワード付きZIPを送ってあとでパスワードを送ってる

```bash
$ echo "UEsDBAoACQAAAOJVm0zEdBgeLQAAACEAAAAIABwAZmxhZy50eHRVVAkAA6f/4lqn/+JadXgLAAEE
AAAAAAQAAAAASsSD0p8jUFIaCtIY0yp4JcP9Nha32VYd2BSwNTG83tIdZyU4x2VJTGyLcFquUEsH
CMR0GB4tAAAAIQAAAFBLAQIeAwoACQAAAOJVm0zEdBgeLQAAACEAAAAIABgAAAAAAAEAAACkgQAA
AABmbGFnLnR4dFVUBQADp//iWnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE4AAAB/AAAAAAA=" | base64 -d > encrypted.zip
$ unzip encrypted.zip
Archive:  encrypted.zip
[encrypted.zip] flag.txt password: _you_are_pro_
 extracting: flag.txt
$ cat flag.txt
ctf4b{email_with_encrypted_file}
```

パスワード付きZIPは悪い文化

`ctf4b{email_with_encrypted_file}`