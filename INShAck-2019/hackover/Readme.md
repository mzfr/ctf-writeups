# HackCode

__Description__

We have a little budgeting issue with our latest red team campaign. Please help us figure it out :

https://hack-code.ctf.insecurity-insa.fr

This challenge has 4 different flags, better solutions will grant you more flags.


__SOLUTION__

I didn't solve this challenge this my actually solved by __@nullpointer__ and __@luca__.

Basically we need to write an algorithm that is efficient. The more efficient the algorith the more flag you'll get.

This challenge had 4 flags.

First __@NullPointer__ wrote a [script](nullpointer.py) with which we was able to get 128 taps which gave us 3 flags.

```
First flag is INSA{N0t_bad_f0r_a_start}. The next flag will be awarded at <= 135.
```

```
INSA{135_is_pretty_g0Od_but_how_l0w_c4n_u_gO}. Get your next flag at <= 128
```

```
INSA{Getting_cl0ser}. The last flag is waiting for you at 126 !
```

After that lot of people started to optimize the algorithm and finally __@luca__ was able to optimize the [script](luca.py) it to give us 126 taps and we got the final flag.
