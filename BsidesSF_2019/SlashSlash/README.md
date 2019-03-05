# SlashSlash

__PROBELM__

/* Zip */

[flag.zip](flag.zip/)

__SOLUTION__

So this was the simplest of them all I think even though I couldn't get the flag even though I was using the correct command.

So after extracting the zip file we'll get a file named `flag.aes128cbc`. We can simply use the `openssl` tool to decrypt it but we'll need a password to do so.

If you check the strings of the zip file you'll find the password

```
➜ strings flag.zip
flag.aes128cbcUT
{\ux
Salted__
flag.aes128cbcUT
{\ux
SevenPinLock0123456
```

The password is `SevenPinLock0123456`.

```
openssl enc -d -aes-128-cbc -pass pass:SevenPinLock0123456 -in flag.aes128cbc
```

