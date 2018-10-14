# Strings

__PROBLEM__

Can you find the flag in this [file](strings) without actually running it? You can also find the file in /problems/strings_4_40d221755b4a0b134c2a7a2e825ef95f on the shell server.

__HINT__

[strings](https://linux.die.net/man/1/strings)

__SOLUTION__

Using the `strings` on the file will give you lot of String but we only want the flag so we do something like
```
strings strings | grep "picoCTF"
```

FLAG - `picoCTF{sTrIngS_sAVeS_Time_d7c8de6c}`
