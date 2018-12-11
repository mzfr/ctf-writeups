# 1-What the password?

__PROBLEM__

you got a sample of rick's PC's memory. can you get his user password? format: CTF{...}

Download link: https://mega.nz/#!sh8wmCIL!b4tpech4wzc3QQ6YgQ2uZnOmctRZ2duQxDqxbkWYipQ

__SOLUTION__

After downloading the file and unpacking it you'll get a file name `OtterCTF.vmem`. Basically this a `PC memory` image(as mentioned in the problem).We need password for the PC.

After googling for a bit I found out that [`volatility`](https://github.com/volatilityfoundation/volatility) is the best tool for such kind of memory forensics. After installing and searching for `password from memory volatility` I found [Volatility/Retrieve-password](https://www.aldeid.com/wiki/Volatility/Retrieve-password). I followed all the steps and got myself hashes.

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Rick:1000:aad3b435b51404eeaad3b435b51404ee:518172d012f97d3a8fcc089615283940:::
```

Now all we have to do is crack the hash. I tried lots of famous online tools like [crackstation](https://crackstation.net/), [hashkiller](https://hashkiller.co.uk/) etc but couldn't crack the password. Then I shifted to [hashcat](https://hashcat.net/hashcat/) and [JTR](https://www.openwall.com/john/) but they were taking too much time.

So I started looking for a better way and found [Volatility & Mimikatz](https://danielsauder.com/2016/02/06/windows-credentials-and-memory-dumps-part-4-volatility-mimikatz/).

Just download that [mimikatz plugin](https://raw.githubusercontent.com/RealityNet/hotoloti/master/volatility/mimikatz.py) and fire it up of the memory.

```bash
➜ volatility --plugin=./volatility-plugins/ -f OtterCTF.vmem --profile=Win7SP1x64 mimikatz
Volatility Foundation Volatility Framework 2.6
Module   User             Domain           Password
-------- ---------------- ---------------- ----------------------------------------
wdigest  Rick             WIN-LO6FAF3DTFE  MortyIsReallyAnOtter
wdigest  WIN-LO6FAF3DTFE$ WORKGROUP

```

And we have the password

FLAG - `CTF{MortyIsReallyAnOtter}`
