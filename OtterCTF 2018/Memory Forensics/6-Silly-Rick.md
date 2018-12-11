# 6-Silly Rick

__PROBLEM__

Silly rick always forgets his email's password, so he uses a Stored Password Services online to store his password. He always copy and paste the password so he will not get it wrong. whats rick's email password?

format: CTF{flag}


__SOLUTION__

If you'll read the statement carefully then you'll notice it is talking about `copy and paste the password`. This mean the password will be present in the `clipboard` of the memory.

```bash
➜ vol.py -f OtterCTF.vmem --profile=Win7SP1x64 clipboard
Volatility Foundation Volatility Framework 2.6
Session    WindowStation Format                         Handle Object             Data
---------- ------------- ------------------ ------------------ ------------------ --------------------------------------------------
         1 WinSta0       CF_UNICODETEXT                0x602e3 0xfffff900c1ad93f0 M@il_Pr0vid0rs
         1 WinSta0       CF_TEXT                          0x10 ------------------
         1 WinSta0       0x150133L              0x200000000000 ------------------
         1 WinSta0       CF_TEXT                           0x1 ------------------
         1 ------------- ------------------           0x150133 0xfffff900c1c1adc0
```

FLAG - `CTF{M@il_Pr0vid0rs}`
