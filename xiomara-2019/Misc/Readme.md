# Story

__PROBLEM__

At Xiomara Tech., we take Cyber Security very seriously. We have been breached, despite our numerous countermeasures and safety precautions. The breach has raised a concern of privacy amongst our clients. Since the past 24hrs, our security and incident response team are working relentlessly to identify the breach. So far it has been discovered that it's an insiders job. We need your help in fighting this breach.

We managed to find this encrypted message, and believe that you can decrypt it dXFjeWFpYXtpMzdfYnZxX2NrZl95M28xYn0=


__SOLUTION__

We can see that it's simple base64 decode

```bash
➜ echo "dXFjeWFpYXtpMzdfYnZxX2NrZl95M28xYn0=" | base64 -d
uqcyaia{i37_bvq_ckf_y3o1b}
```

Now it's simple Vignere Cipher with `xiomara` as the key

Use [Cryptii](https://cryptii.com/pipes/vigenere-cipher) to get the flag.

__How to know it's vignere and what's the key?__

Simple guessing and random trys. I first tried rot13 then caesar that did gave any result so I just tried vignere.

FLAG: `xiomara{l37_the_ctf_b3g1n}`
