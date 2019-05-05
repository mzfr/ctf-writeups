# You Shall Not Pass

__DESCRIPTION__

One of my friends is a show-off and I don't like that.

Help me find the backdoor he just boasted about! :D

You'll find an image of his USB key [here](https://static.ctf.insecurity-insa.fr/3b89ef8bb51773c8f3478bf356271ac762ec96c3.tar.gz).

And one last thing, my friend owns you-shall-not-pass.ctf.insecurity-insa.fr


__SOLUTION__

Since this was a disk image the first thing I did was to run testdisk on it but I got some bootsector error. So I tried with photorec which recover a mp4.
Then __@unblvr__ used sleuth kit to carved the files and found a base64 in the slack space of the mp4 file.

```
-BGZ-H4sIAOq1yVwAA6tWUFBKyc8vUrJSMDIAAh0gvzi1sDQ1LzkVKBatAATVSgX5RSVAnqGBgSFQhVJB
UX5JPpCvFOoSoFSrg67Gkgg1RihqQpyxqSHGLjMizLEgwhxi7DIgwi4DIswxIcIcI0xzFBRiQbGT
X5CaF1+cWpyYC4ogJXdPX19XhRAPVwU3H0d3hQCfKD09PSVoNMZn5pWkFpUl5oAN1YHGNbKoaS0A
gssCMwICAAA=
```

If you decode this base64 this will give you a `gzip` file and inside that gzip we found a dictionary.

```json
{  "door": 20000,  "sequence": [    {"port": 10010, "proto": "UDP"},    {"port": 10090, "proto": "UDP"},    {"port": 10020, "proto": "TCP"},    {"port": 10010, "proto": "UDP"},    {"port": 10060, "proto": "TCP"},    {"port": 10080, "proto": "UDP"},    {"port": 10010, "proto": "UDP"},    {"port": 10000, "proto": "TCP"},    {"port": 10000, "proto": "UDP"},    {"port": 10040, "proto": "TCP"},    {"port": 10020, "proto": "UDP"}  ],  "open_sesame": "GIMME THE FLAG PLZ...",  "seq_interval": 10,  "door_interval": 5}
```

Now looking at this dictionary we could guess that it's some port knocking thing.
At first we were confuse that we might have to guess the right sequence and we have to give 10sec delay between each delay and stuff but then after talking to admins we found out that we just need to follow the default sequence.

The whole thing is we have to go to each port, just make connection and then for 5 sec the door port i.e 20000 opens, we have to connect to it and send the `GIMME THE FLAG PLZ...` strings and we'll get the flag.

I wrote a script for trying this out but my script didn't worked as I kept getting `Connection Refused` when trying to connect to `door`.

The __@unblvr__ wrote a [script](knockknock.py) which worked.

So You can run this script and the moment it stop, do the following

```bash
➜ nc you-shall-not-pass.ctf.insecurity-insa.fr 20000
GIMME THE FLAG PLZ...
INSA{213dca08e606ef9e5352f4bdd8b6dd9d6c559e9ce76b674ae3739a34c5c3be37}
```

`FLAG`: INSA{213dca08e606ef9e5352f4bdd8b6dd9d6c559e9ce76b674ae3739a34c5c3be37}


P.S:

The funny that happened during this challenge was that when we found the dictionary having all the ports and stuff I thought of doing pot scan of the gven server because I thought this would invole some kind of hacking etc.

I found out that there was this version `ISC BIND 9.11.3`. Then I found out https://www.tenable.com/plugins/nessus/119264
So I thought we might have to exploit this CVE so I asked the admin about this. And the result of that was:

![alt text](nope.png)
