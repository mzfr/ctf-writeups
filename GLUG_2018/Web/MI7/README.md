# MI7

__PROBLEM__

Olny Agents are allowed.
[Link](https://mi7secret-glugctf.netlify.com/)

__SOLUTION__

After visiting the page and reading `Even Google is allowed to see our secrets. You are not an agent! How dare you, to be here !!` first thing that hits our mind is `Hey lets change our user agent to google.com` but that is not the case.

Just check out the `robots.txt` for the give website and we see:

```
User-agent: *
Disallow: /cyberworld/map/
Disallow: /tmp/
Disallow: /fsck.bf
Disallow: /a7_vault.html
Disallow: /exploits/fuzzbunch/Eternal_pink
Disallow: /exploits/network/QuantumInjection.pdf
```

Then just head over to `https://mi7secret-glugctf.netlify.com/a7_vault.html`
you'll see `R0xVR3tiMDc1X2M0bl8xNm4wcjNfN2gzX3J1bDM1fQ==` and that's base64 encode. Decode it to get the flag.

FLAG - `GLUG{b075_c4n_16n0r3_7h3_rul35}`
