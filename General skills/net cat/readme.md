# net cat

__PROBLEM__

Using netcat (nc) will be a necessity throughout your adventure. Can you connect to 2018shell2.picoctf.com at port 22847 to get the flag?

__HINT__

nc [tutorial](https://linux.die.net/man/1/nc)

__SOLUTION__

All you have to do is use netcat to connect to the given service on a given port:
```bash
nc 2018shell2.picoctf.com 22847

That wasn't so hard was it?
picoCTF{NEtcat_iS_a_NEcESSiTy_69222dcc}
```

FLAG - `picoCTF{NEtcat_iS_a_NEcESSiTy_69222dcc}`
