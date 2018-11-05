# hertz 2

__PROBLEM__

 This flag has been encrypted with some kind of cipher, can you decrypt it? Connect with nc 2018shell1.picoctf.com 18990.

__HINT__

These kinds of problems are solved with a frequency that merits some analysis.

__SOLUTION__

Connecting to service we get:
```
Nqm fyrjb whaxc sae gytpd aomh nqm ilzu kav. R jlc'n wmirmom nqrd rd dyjq lc mldu phawimt rc Prja. Rn'd litadn ld rs R daiomk l phawimt lihmlku! Ablu, srcm. Qmhm'd nqm silv: prjaJNS{dywdnrnynrac_jrpqmhd_lhm_naa_mldu_qqwqvtaaka}
```

Our first step is to be identify what kind of cipher the message has been encoded.
To identify an unknow cipher there is this method called finding Index of coincidence(I.C). Read about I.C [here](http://practicalcryptography.com/cryptanalysis/text-characterisation/identifying-unknown-ciphers/).

Then I used online [I.C calculator](http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/).

We get I.C = `0.05450693374422188` which tells us that it is also a subsitution cipher.

So again going to our beloved [decoder](https://www.guballa.de/substitution-solver) and we get the flag.

FLAG - `picoCTF{substitution_ciphers_are_too_easy_hhbhgmoodo}`
